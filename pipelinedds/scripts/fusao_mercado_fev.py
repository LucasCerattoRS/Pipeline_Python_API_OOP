from pathlib import Path
from processamento_dados import Dados  # Importamos o nosso "Molde"

# --- CONFIGURAÇÃO DE CAMINHOS ---
FILE_PATH = Path(__file__).resolve()
DIR_PROJECT = FILE_PATH.parent.parent
PATH_RAW = DIR_PROJECT / 'data_raw'
PATH_PROCESSED = DIR_PROJECT / 'data_processed'

# Mapeamento de colunas
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# --- O PIPELINE ---
def pipeline_principal():
    
    # 1. EXTRACT (Usando o Molde 'Dados')
    print("Iniciando leitura...")
    
    # Criamos o objeto da Empresa A
    # O __init__ corre sozinho e já carrega os dados!
    dados_empresa_A = Dados(PATH_RAW / 'dados_empresaA.json', 'json')
    print(f"Empresa A carregada: {dados_empresa_A.qtd_linhas} linhas")

    # Criamos o objeto da Empresa B
    dados_empresa_B = Dados(PATH_RAW / 'dados_empresaB.csv', 'csv')
    print(f"Empresa B carregada: {dados_empresa_B.qtd_linhas} linhas")

    # 2. TRANSFORM
    print("Transformando dados...")
    
    # Mandamos o objeto B renomear as suas próprias colunas
    dados_empresa_B.rename_columns(key_mapping)
    
    # Juntamos A com B
    # O método .join cria um terceiro objeto com tudo misturado
    dados_fusao = dados_empresa_B.join(dados_empresa_A)
    print(f"Fusão completa: {dados_fusao.qtd_linhas} linhas")

    # 3. LOAD
    path_saida = PATH_PROCESSED / 'dados_combinados.csv'
    dados_fusao.salvando_dados(path_saida)

if __name__ == "__main__":
    pipeline_principal()