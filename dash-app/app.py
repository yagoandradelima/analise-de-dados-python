# Dash - Pacote da biblioteca de dash. É um import padrão que deve sempre ser realizado
# html - Import padrão. Ele permite manipular o html do app (que tecnicamente seria um site)
# dash_table - Permite a visualização de Data Frames em forma de tabelas (e outros dados também)
# dcc - Import para publicar gráficos np app
from dash import Dash, html, dash_table, dcc
import pandas as pd

# Código Padrão para inicializar o app
app = Dash(__name__)

#Incorporando dados
df = pd.read_csv('tatamotorsstockprices.csv')

# Layout do app
app.layout = html.Div([
            html.Div(children='Hello World'),
            dash_table.DataTable(data=df.to_csv('tatamotorsstockprices2.csv'))
            ])

# Rodar o app
if __name__ == '__main__':
    app.run(debug=True)