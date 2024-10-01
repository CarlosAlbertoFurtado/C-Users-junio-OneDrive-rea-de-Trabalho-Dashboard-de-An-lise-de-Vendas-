import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Carrega o arquivo CSV com os dados de vendas
df = pd.read_csv('dados_vendas.csv')

# Adiciona uma coluna com o valor total de cada venda
df['Total Venda'] = df['Quantidade'] * df['Valor']

# Agrupa por produto para calcular o total de vendas por produto
vendas_por_produto = df.groupby('Produto')['Total Venda'].sum().reset_index()

# Agrupa por categoria para calcular o total de vendas por categoria
vendas_por_categoria = df.groupby('Categoria')['Total Venda'].sum().reset_index()

# Agrupa as vendas por data
df['Data da Venda'] = pd.to_datetime(df['Data da Venda'])
vendas_por_data = df.groupby('Data da Venda')['Total Venda'].sum().reset_index()

# Criação dos gráficos com Plotly
fig_produto = px.bar(vendas_por_produto, x='Produto', y='Total Venda', title='Vendas por Produto')
fig_categoria = px.bar(vendas_por_categoria, x='Categoria', y='Total Venda', title='Vendas por Categoria')
fig_tempo = px.line(vendas_por_data, x='Data da Venda', y='Total Venda', title='Vendas ao Longo do Tempo')

# Inicializa a aplicação
app = Dash(__name__)

# Layout do dashboard
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Vendas'),

    # Gráfico de vendas por produto
    html.Div(children=[
        html.H2('Vendas por Produto'),
        dcc.Graph(
            id='grafico-produto',
            figure=fig_produto
        )
    ]),

    # Gráfico de vendas por categoria
    html.Div(children=[
        html.H2('Vendas por Categoria'),
        dcc.Graph(
            id='grafico-categoria',
            figure=fig_categoria
        )
    ]),

    # Gráfico de vendas ao longo do tempo
    html.Div(children=[
        html.H2('Vendas ao Longo do Tempo'),
        dcc.Graph(
            id='grafico-tempo',
            figure=fig_tempo
        )
    ]),
])

# Roda o servidor do Dash
if __name__ == '__main__':
    app.run_server(debug=True)

