from os import listdir, path
from pandas import DataFrame, read_csv
import plotly.express as px

diretorio = r'C:\\Users\User\Downloads\Vendas'
listaArquivos = listdir(diretorio)

# Cria uma tabela vazia
totalTabela = DataFrame()

for arquivo in listaArquivos:
    if 'vendas' in arquivo.lower():
        #caminho do arquivo
        caminhoArq = path.join(diretorio, arquivo)
        tabela = read_csv(caminhoArq)
        totalTabela = totalTabela._append(tabela)

# Separação da do produtos e a soma das quantidades vendidas
tabelaProdutos = totalTabela.groupby('Produto').sum()[['Quantidade Vendida']]
tabelaProdutos = tabelaProdutos.sort_values(by = 'Quantidade Vendida', ascending = False)

# Visualização do produto que mais faturou
totalTabela['Faturamento'] = totalTabela['Quantidade Vendida'] * totalTabela['Preco Unitario']
fatTotal = totalTabela.groupby('Produto').sum()
fatTotal = fatTotal[['Faturamento']].sort_values(by = 'Faturamento', ascending = False)

# Visualização da loja que mais vendeu
totalTabela['Loja'] = totalTabela['Loja']
lojaTotal = totalTabela.groupby('Loja').sum()[['Faturamento']]

# Dashboard
lojaTotal = lojaTotal.reset_index()
grafico = px.bar(lojaTotal, x = 'Loja' , y = 'Faturamento', title = 'Faturamento por loja')
grafico.show()
grafico.write_html('grafico.html')