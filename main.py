import dash
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt 
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
estado_sp = pd.DataFrame(pd.read_csv("Dados-covid-19-estado.csv", delimiter = ";", encoding="latin1", low_memory = False))
municipios_sp = pd.DataFrame(pd.read_csv("Dados-covid-19-municipios.csv", delimiter = ";", encoding="latin1", low_memory = False))

preexistentes_0 = pd.DataFrame(pd.read_csv("parte_0.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_1 = pd.DataFrame(pd.read_csv("parte_1.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_2 = pd.DataFrame(pd.read_csv("parte_2.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_3 = pd.DataFrame(pd.read_csv("parte_3.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_4 = pd.DataFrame(pd.read_csv("parte_4.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_5 = pd.DataFrame(pd.read_csv("parte_5.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_6 = pd.DataFrame(pd.read_csv("parte_6.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_7 = pd.DataFrame(pd.read_csv("parte_7.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_8 = pd.DataFrame(pd.read_csv("parte_8.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_9 = pd.DataFrame(pd.read_csv("parte_9.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_10 = pd.DataFrame(pd.read_csv("parte_10.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_11 = pd.DataFrame(pd.read_csv("parte_11.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_12 = pd.DataFrame(pd.read_csv("parte_12.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_13 =pd.DataFrame(pd.read_csv("parte_13.csv", delimiter = ";", encoding="latin1", low_memory = False))
preexistentes_14 =pd.DataFrame(pd.read_csv("parte_14.csv", delimiter = ";", encoding="latin1", low_memory = False))

all_preexistentes = [estado_sp, municipios_sp,preexistentes_0,preexistentes_1,preexistentes_2,preexistentes_3,preexistentes_4,preexistentes_5, preexistentes_6,preexistentes_7,preexistentes_8, preexistentes_9, preexistentes_10, preexistentes_11, preexistentes_12, preexistentes_13, preexistentes_14]
#all_datas = [estado_sp, municipios_sp, all_preexistentes]
doencas_pre_existentes = pd.concat(all_preexistentes)


"""listadados = [estado_sp, municipios_sp, doencas_pre_existentes]
dados = pd.DataFrame(pd.concat(listadados))

relacao_casos_obitos = pd.read_csv('Dados-covid-19-estado.csv')

# Extrair as colunas de casos por dia e óbitos por dia
casos_por_dia = relacao_casos_obitos['Casos_por_dia']
obitos_por_dia = relacao_casos_obitos['obitos_por_dia']

# Criar um gráfico de dispersão
plt.scatter(casos_por_dia, obitos_por_dia)

# Adicionar rótulos e título ao gráfico
plt.xlabel('Casos por dia')
plt.ylabel('Óbitos por dia')
plt.title('Relação entre Casos por dia e Óbitos por dia')


# Carregar os dados do arquivo CSV
relacao_casos_obitos = pd.read_csv('Dados-covid-19-estado.csv')


# Extrair as colunas de casos por dia e óbitos por dia
casos_por_dia = relacao_casos_obitos['Casos_por_dia']
obitos_por_dia = relacao_casos_obitos['obitos_por_dia']







# Definir o layout do dashboard
app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Dashboard de COVID-19"),
        dcc.Graph(
            id="grafico-barras-agrupadas",
            figure=go.Figure(
                data=[
                    go.Bar(x=relacao_casos_obitos.index, y=casos_por_dia, name='Casos por dia'),
                    go.Bar(x=relacao_casos_obitos.index, y=obitos_por_dia, name='Óbitos por dia')
                ],
                layout=go.Layout(
                    title='Casos por dia e Óbitos por dia',
                    barmode='group'
                )
            )
        )
    ]
)

# Executar o dashboard
if __name__ == '__main__':
    app.run_server(debug=True)
"""