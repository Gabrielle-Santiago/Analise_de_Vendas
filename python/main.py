from os import listdir, path
from pandas import DataFrame, read_csv
import plotly.express as px

diretorio = r'C:\\Users\User\Downloads\Vendas'
listaArquivos = listdir(diretorio)

totalTabela = DataFrame()

for arquivo in listaArquivos:
    if 'vendas' in arquivo.lower():
        #caminho do arquivo
        caminhoArq = path.join(diretorio, arquivo)
        tabela = read_csv(caminhoArq)
        totalTabela = totalTabela._append(tabela)

# Separação dos produtos e a soma das quantidades vendidas
tabelaProdutos = totalTabela.groupby('Produto').sum()[['Quantidade Vendida']]
tabelaProdutos = tabelaProdutos.sort_values(by = 'Quantidade Vendida', ascending = False)

# Informações gerais dos produtos
infoProdutos = totalTabela[["Produto", "Quantidade Vendida", "Preco Unitario"]]
infoProdutos = infoProdutos.merge(tabelaProdutos, on='Produto', suffixes=('_total', '_produto'))
infoProdutos_agrupados = infoProdutos.groupby('Produto').sum().reset_index
print(infoProdutos_agrupados)

# Visualização do produto que mais faturou
totalTabela['Faturamento'] = totalTabela['Quantidade Vendida'] * totalTabela['Preco Unitario']
fatTotal = totalTabela.groupby('Produto').sum()
fatTotal = fatTotal[['Faturamento']].sort_values(by = 'Faturamento', ascending = False)

# Visualização da loja que mais vendeu
totalTabela['Loja'] = totalTabela['Loja']
lojaTotal = totalTabela.groupby('Loja').sum()[['Faturamento']]

# Dashboard
"""lojaTotal = lojaTotal.reset_index()
grafico = px.bar(lojaTotal, x = 'Loja' , y = 'Faturamento', title = 'Faturamento por loja')
grafico.show()
grafico.write_html('\html\grafico.html')"""