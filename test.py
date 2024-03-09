import os
import pandas as pd

# Diretório contendo os arquivos CSV
diretorio = r'C:\\Users\User\Downloads\Vendas'

# Lista todos os arquivos no diretório
listaArquivos = os.listdir(diretorio)

# Itera sobre os arquivos
for arquivo in listaArquivos:
    # Verifica se o nome do arquivo contém 'vendas' (ignorando maiúsculas e minúsculas)
    if 'vendas' in arquivo.lower():
        # Constrói o caminho completo do arquivo usando os.path.join()
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        # Tenta ler o arquivo CSV
        try:
            tabela = pd.read_csv(caminho_arquivo)
            print(tabela)
        except Exception as e:
            print(f"Erro ao ler o arquivo {arquivo}: {e}")
