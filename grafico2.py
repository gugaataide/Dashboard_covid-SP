import dash
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt 
from dash import html, dcc
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Ler o arquivo CSV
dados = pd.read_csv('casos_obitos_doencas_preexistentes.csv')

# Contar o número de pacientes por sexo
contagem_sexo = dados['cs_sexo'].value_counts()

# Contar o número de pacientes com diagnóstico de COVID-19
contagem_covid = dados['diagnostico_covid19'].value_counts()

# Criar o gráfico de pizza para a distribuição por sexo
fig_sexo = go.Figure(data=[go.Pie(labels=contagem_sexo.index, values=contagem_sexo.values)])
fig_sexo.update_layout(title_text='Distribuição por Sexo')

# Criar o gráfico de pizza para o diagnóstico de COVID-19
fig_covid = go.Figure(data=[go.Pie(labels=contagem_covid.index, values=contagem_covid.values)])
fig_covid.update_layout(title_text='Diagnóstico COVID-19')

# Criar o dashboard com os gráficos
dashboard = make_subplots(rows=1, cols=2, subplot_titles=('Distribuição por Sexo', 'Diagnóstico COVID-19'))
dashboard.add_trace(fig_sexo.data[0], row=1, col=1)
dashboard.add_trace(fig_covid.data[0], row=1, col=2)

dashboard.update_layout(height=600, showlegend=False)
dashboard.show()

dcc.Graph(
            id="grafico-barras-agrupadas",
            figure=go.Figure(
                data=[
                    go.Bar(x=relacao_casos_por_sexo.index, y=contagem_sexo, name='cs_sexo'),
                    go.Bar(x=relacao_casos_por_sexo.index, y=contagem_covid, name='Óbitos por dia')
                ],
                layout=go.Layout(
                    title='Casos por dia e Óbitos por dia',
                    barmode='group'
                )
            )
