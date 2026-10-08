# Pipeline Python + POO

Três exercícios de curso de Python, guardados juntos para estudo:

1. **`pipelinedds/`** — um mini ETL: lê os produtos de uma "empresa A" (JSON) e de
   uma "empresa B" (CSV), padroniza os nomes das colunas, junta tudo e salva um CSV.
2. **`poo-api/`** — primeira versão de um modelo de restaurante com classes simples
   (`Restaurante`, `Avaliacao`).
3. **`python-oop-api/stepapiopp/`** — versão evoluída, com cardápio em hierarquia:
   classe abstrata `ItemCardapio` e as filhas `Prato` e `Bebida`.

"API" no nome é o desenho das classes que uma API usaria; não há servidor.

## Estado

Concluído como exercício. Os três scripts rodam. Em 08/10/2026 foram corrigidos dois
bugs da etapa 3 (`exibir_cardapio()` dava `TypeError`; a classe "abstrata" podia ser
instanciada) e foram criados testes para eles.

## Como rodar

Só biblioteca padrão. Precisa de **Python 3.12+** (o `restaurante.py` usa aspas
simples dentro de f-string de aspas simples, o que só é válido a partir do 3.12).

Windows (PowerShell):

```powershell
python pipelinedds\scripts\fusao_mercado_fev.py      # gera pipelinedds\data_processed\dados_combinados.csv
cd poo-api; python app.py; cd ..
cd python-oop-api\stepapiopp; python app.py; python -m unittest -v; cd ..\..
```

Linux:

```bash
python3 pipelinedds/scripts/fusao_mercado_fev.py
(cd poo-api && python3 app.py)
(cd python-oop-api/stepapiopp && python3 app.py && python3 -m unittest -v)
```

Se o terminal do Windows mostrar caracteres estranhos (☐, ç), rode antes
`$env:PYTHONIOENCODING="utf-8"`.

Saída esperada do pipeline: 3123 linhas (A) + 1323 linhas (B) = 4446 linhas combinadas.

## Estrutura

| Caminho | O que é |
|---|---|
| `pipelinedds/scripts/processamento_dados.py` | Classe `Dados`: lê CSV/JSON/lista, renomeia colunas, junta e salva. |
| `pipelinedds/scripts/fusao_mercado_fev.py` | O pipeline (extract → transform → load) usando `Dados`. |
| `pipelinedds/data_raw/` | Dados de entrada fictícios. |
| `pipelinedds/data_processed/` | Saída gerada pelo pipeline (versionada para consulta). |
| `pipelinedds/notebooks/exoloration.ipynb` | Exploração em Jupyter. |
| `poo-api/` | Restaurante + avaliações (POO básica). |
| `python-oop-api/stepapiopp/` | Restaurante + cardápio (herança, classe abstrata, polimorfismo) e `test_modelos.py`. |
| `docs/estudo/ROTEIRO.md` | Roteiro de estudo com exercícios. |

## Tecnologias

Python 3.12 · `csv` · `json` · `pathlib` · `abc` · `unittest`. Nenhuma dependência externa.

## Pendências

- `python-oop-api/stepapiopp/requirements.txt` lista FastAPI, requests etc., mas
  nenhum código usa: dá para ignorar (ou apagar) esse arquivo.
- `receber_avaliacao` aceita só nota de 1 a 5 e **ignora em silêncio** o resto: em
  `poo-api/app.py` as notas 10 e 8 são descartadas e a média sai 2.0.
- `Dados.get_columns` olha só a primeira linha; o pipeline funciona porque a empresa
  B (que tem "Data da Venda") vem primeiro no `join`. Na ordem inversa, o
  `DictWriter` quebraria.
- `leitura_dados` engole erros de leitura (imprime e segue com lista vazia).

## Para estudar

1. **Construtor que já trabalha** — `pipelinedds/scripts/processamento_dados.py:9-17`:
   o `__init__` lê o arquivo, descobre colunas e conta linhas na hora.
2. **Renomear colunas com dicionário e `.get(chave, padrão)`** —
   `processamento_dados.py:52-71`: o que não está no mapa passa igual.
3. **Classe abstrata de verdade** — `python-oop-api/stepapiopp/modelos/cardapio/item_cardapio.py:2-15`:
   `ABC` + `@abstractmethod` obrigam cada filha a implementar `aplicar_desconto`.
4. **Polimorfismo com `isinstance`** — `python-oop-api/stepapiopp/modelos/restaurante.py:48-53`:
   o restaurante aceita qualquer `ItemCardapio` sem saber se é prato ou bebida.

Mais em [`docs/estudo/ROTEIRO.md`](docs/estudo/ROTEIRO.md).
