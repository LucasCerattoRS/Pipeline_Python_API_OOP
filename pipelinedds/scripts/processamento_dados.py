import csv
import json

class Dados:
    """
    Classe que serve de molde para ler, transformar e salvar dados.
    """

    def __init__(self, caminho, tipo_dados):
        """
        Esta função corre automaticamente quando crias um novo objeto 'Dados'.
        É como ligar a máquina: ela guarda o caminho e lê logo o ficheiro.
        """
        self.caminho = caminho
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados() # Lê os dados imediatamente
        self.nome_colunas = self.get_columns() # Descobre os nomes das colunas
        self.qtd_linhas = self.size_data()     # Conta as linhas

    def leitura_dados(self):
        dados = []
        if self.tipo_dados not in ('csv', 'json', 'list'):
            raise ValueError(f"tipo_dados inválido: {self.tipo_dados!r}")
        # Sem try/except: arquivo ausente ou JSON quebrado deve parar o pipeline,
        # em vez de seguir com lista vazia e gravar um CSV vazio como se fosse sucesso.
        if self.tipo_dados == 'csv':
            with open(self.caminho, 'r', encoding='utf-8') as ficheiro:
                leitor = csv.DictReader(ficheiro, delimiter=',')
                for linha in leitor:
                    dados.append(linha)
            
        elif self.tipo_dados == 'json':
            with open(self.caminho, 'r', encoding='utf-8') as ficheiro:
                dados = json.load(ficheiro)
            
        elif self.tipo_dados == 'list':
            # Caso especial para quando já temos uma lista na memória
            dados = self.caminho
            self.caminho = "Lista em Memória"

        # JSON/lista fora do formato esperado quebrava depois, com erro obscuro (ou passava com colunas lixo)
        if not isinstance(dados, list) or not all(isinstance(l, dict) for l in dados):
            raise ValueError("os dados devem ser uma lista de objetos (dict)")
        return dados

    def get_columns(self):
        # União das colunas de todas as linhas, na ordem em que aparecem
        colunas = {}
        for linha in self.dados:
            colunas.update(dict.fromkeys(linha))
        return list(colunas)

    def size_data(self):
        return len(self.dados)

    def rename_columns(self, key_mapping):
        """
        A nossa versão simplificada da tradução de colunas.
        """
        novos_dados = []

        # O self.dados é a "memória" deste objeto específico
        for linha_antiga in self.dados:
            linha_temp = {}
            for coluna_velha, valor in linha_antiga.items():
                
                # Tenta traduzir, se não conseguir, mantém o original
                coluna_nova = key_mapping.get(coluna_velha, coluna_velha)
                linha_temp[coluna_nova] = valor
            
            novos_dados.append(linha_temp)
        
        # Atualiza a memória do objeto com os dados novos
        self.dados = novos_dados
        self.nome_colunas = self.get_columns()

    def join(self, outros_dados):
        """
        Junta os dados DESTE objeto com os dados de OUTRO objeto.
        """
        lista_combinada = self.dados + outros_dados.dados
        
        # Retorna um NOVO objeto Dados com o resultado da soma
        return Dados(lista_combinada, 'list')

    def salvando_dados(self, caminho_saida):
        # Garante que a pasta existe
        caminho_saida.parent.mkdir(parents=True, exist_ok=True)
        
        colunas = self.get_columns()
        
        with open(caminho_saida, 'w', newline='', encoding='utf-8') as ficheiro:
            writer = csv.DictWriter(ficheiro, fieldnames=colunas, restval='')
            writer.writeheader()
            writer.writerows(self.dados)
        
        print(f"Dados salvos em: {caminho_saida}")