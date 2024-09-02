# Dash - Pacote da biblioteca de dash. É um import padrão que deve sempre ser realizado
# html - Import padrão. Ele permite manipular o html do app (que tecnicamente seria um site)
# dash_table - Permite a visualização de Data Frames em forma de tabelas (e outros dados também)
# dcc - Import para publicar gráficos np app
from dash import Dash, html, dash_table, dcc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Código Padrão para inicializar o app
app = Dash(__name__)

#Incorporando dados
df = pd.read_csv('tatamotorsstockprices.csv')

# Layout do app
app.layout = html.Div([
            # Incorporando um texto inicial simples
            html.Div(children='Hello World'),

            # Plotando o primeiro gráfico criado no Jupyter Notebook dentro dessa pasta
            dcc.Graph(figure= px.line(
                            df,
                            x='Date',
                            y='Adj Close',
                            labels={'Date':'Data', 'Adj Close':'Fechamento Ajustado'},
                            title='Preço das Ações - Tata Motors'
    
    # Deixando o rangeslider visível e utilizável no gráfico de linha
    ).update_xaxes(rangeslider_visible=True)
),
            # Plotando o segundo gráfico de candlestick criado no Jupyter Notebook dessa pasta
            dcc.Graph(figure = go.Figure(
                                data=go.Candlestick(
                                    x=df['Date'],
                                    open=df['Open'],
                                    high=df['High'],
                                    low=df['Low'],
                                    close=df['Close']
    )

# Update do layout do gráfico de Candlestick para modificar os nomes dos eixos e título
).update_layout(
    title='Tata Motors Stock Prices',
    yaxis_title='Stock Prices',
    xaxis_title='Data'
    )
)
            ])

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)