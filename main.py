from os import listdir, path
import pandas as pd

diretorio = r'C:\\Users\User\Downloads\Vendas'
listaArquivos = listdir(diretorio)

for arquivo in listaArquivos:
    if 'vendas' in arquivo.lower():
        #caminho do arquivo
        caminhoArq = path.join(diretorio, arquivo)
        tabela = pd.read_csv(caminhoArq)
        print(tabela)
        