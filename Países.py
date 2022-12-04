import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import json
import requests
from streamlit_lottie import st_lottie
import plotly.figure_factory as ff


dv = pd.read_excel('DataCharts.xlsx')

st.title('Rank Paises más visitados')

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_ahlkj7sh.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high 
    height=None,
    width=None,
    key=None,
)

boxes = {'Rank' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20,21,21,21,21,21,22,23,23,24,24,24,24,24],
        'Paises Destino': ['MEX','CAN','FRA','ALE','ESP','ITA','ING','EUA','CHN','SUI','AUS','CZE','CHI','JAP','DIN','POL','CHL','NZL','FIN','ARG','HOL','SUE','BEL','COR','HUN','SVK','nen','TAI','CRO','SAF','COL','HKG','NOR','POR','SIN'],
        'Cantidad de Estudiantes': [1603,1589,1202,956,544,451,420,326,301,178,169,80,37,34,30,29,11,9,7,6,6,6,5,5,5,5,5,3,2,2,1,1,1,1,1]
        }
dh = pd.DataFrame(boxes)



fig3 = go.Figure(data=[go.Table(
    header=dict(values=list(dh.columns),
                fill_color='steelblue',
                align='left'),
    cells=dict(values=[dh['Rank'],dh['Paises Destino'], dh['Cantidad de Estudiantes']],
               fill_color='skyblue',
               align='left'))
])

st.header('Tabla del Ranking 🌎')


#st.plotly_chart(fig3, use_container_width=True)

colorscale = [[0, '#4d004c'],[.5, '#f2e5ff'],[1, '#ffffff']]


fig7 = ff.create_table(dh, colorscale=colorscale)




st.plotly_chart(fig7, use_container_width=True)