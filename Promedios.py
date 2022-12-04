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

dv = pd.read_excel('IntentoE.xlsx')

st.header('Promedios Asignados por Escuela 🏫')


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_omn51ec8.json')

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


st.subheader('Seleccione dentro del gráfico la Escuela que le interese ⤵')
fig6 = px.sunburst(dv, path=['Escuela','promedio_range'], values='PuntajeAsignación')
st.plotly_chart(fig6, use_container_width=True)








