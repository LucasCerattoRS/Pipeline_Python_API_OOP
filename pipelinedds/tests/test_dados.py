"""Testes do pipeline (sem rede, só arquivos temporários).

Rodar na raiz: python -m unittest discover -s pipelinedds/tests -v
"""
import contextlib
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
from processamento_dados import Dados  # noqa: E402
import fusao_mercado_fev  # noqa: E402


class TestDados(unittest.TestCase):
    def test_arquivo_inexistente_levanta_erro(self):
        # Antes: imprimia o erro e seguia com 0 linhas (CSV vazio "com sucesso").
        with self.assertRaises(FileNotFoundError):
            Dados(Path("nao_existe.csv"), "csv")

    def test_tipo_invalido_levanta_erro(self):
        with self.assertRaises(ValueError):
            Dados([], "xml")

    def test_colunas_sao_uniao_de_todas_as_linhas(self):
        d = Dados([{"a": 1}, {"a": 2, "b": 3}], "list")
        self.assertEqual(d.nome_colunas, ["a", "b"])

    def test_salvar_com_colunas_extras_nao_quebra(self):
        d = Dados([{"a": 1}, {"a": 2, "b": 3}], "list")
        with tempfile.TemporaryDirectory() as tmp:
            saida = Path(tmp) / "x" / "out.csv"
            d.salvando_dados(saida)
            with open(saida, encoding="utf-8", newline="") as f:
                linhas = list(csv.DictReader(f))
        self.assertEqual(linhas, [{"a": "1", "b": ""}, {"a": "2", "b": "3"}])

    def test_join_independe_da_ordem(self):
        a = Dados([{"x": 1}], "list")
        b = Dados([{"x": 2, "data": "d"}], "list")
        self.assertEqual(a.join(b).qtd_linhas, 2)
        self.assertEqual(b.join(a).qtd_linhas, 2)

    def _json_temp(self, texto):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        caminho = Path(tmp.name) / "entrada.json"
        caminho.write_text(texto, encoding="utf-8")
        return caminho

    def test_json_invalido_ou_vazio_levanta_erro(self):
        for texto in ('[{"a": 1', ""):
            with self.subTest(texto=texto):
                with self.assertRaises(ValueError):  # JSONDecodeError herda de ValueError
                    Dados(self._json_temp(texto), "json")

    def test_json_que_nao_e_lista_de_objetos_levanta_erro(self):
        # Antes: '[1, 2]' dava TypeError obscuro e '{"a": 1}' era aceito com colunas lixo.
        for texto in ('[1, 2]', '{"a": 1}', '[{"a": 1}, 2]'):
            with self.subTest(texto=texto):
                with self.assertRaisesRegex(ValueError, "lista de objetos"):
                    Dados(self._json_temp(texto), "json")

    def test_lista_em_memoria_invalida_levanta_erro(self):
        with self.assertRaisesRegex(ValueError, "lista de objetos"):
            Dados([1, 2], "list")


class TestPipeline(unittest.TestCase):
    """Roda o pipeline de verdade (dados de data_raw), gravando numa pasta temporária."""

    def _rodar_pipeline(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        original = fusao_mercado_fev.PATH_PROCESSED
        fusao_mercado_fev.PATH_PROCESSED = Path(tmp.name)
        self.addCleanup(setattr, fusao_mercado_fev, "PATH_PROCESSED", original)
        with contextlib.redirect_stdout(io.StringIO()):
            fusao_mercado_fev.pipeline_principal()
        return Path(tmp.name) / "dados_combinados.csv"

    def test_saida_tem_4446_linhas_e_colunas_padronizadas(self):
        with open(self._rodar_pipeline(), encoding="utf-8", newline="") as f:
            leitor = csv.DictReader(f)
            linhas = list(leitor)
        self.assertEqual(len(linhas), 3123 + 1323)
        self.assertEqual(leitor.fieldnames, [
            "Nome do Produto", "Categoria do Produto", "Preço do Produto (R$)",
            "Quantidade em Estoque", "Filial", "Data da Venda",
        ])

    def test_saida_igual_a_versionada_e_com_lf(self):
        # O CSV em data_processed/ é versionado "para consulta": precisa bater byte a byte
        # com o que o pipeline gera. Antes, o csv gravava CRLF e o arquivo sempre aparecia modificado.
        gerado = self._rodar_pipeline().read_bytes()
        versionado = (fusao_mercado_fev.DIR_PROJECT / "data_processed" / "dados_combinados.csv").read_bytes()
        self.assertNotIn(b"\r", gerado)
        self.assertEqual(gerado, versionado)


if __name__ == "__main__":
    unittest.main()
