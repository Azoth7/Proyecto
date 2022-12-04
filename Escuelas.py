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


dv = pd.read_excel('DataCharts.xlsx')



st.title("Internacionalidad por Escuela")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_uqsv3ztj.json")

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



with st.expander('Distribución de Internacionalidad'):
    column25, column12 = st.columns([3,1])
        
    # Allow the user to select 
    selected_level = st.radio('What is your Level:', dv.Nivel.unique(), index = 0)

    # Apply  filter.
    gender_product = dv[dv['Nivel'] == selected_level]

    fig5 = px.histogram(gender_product.sort_values('Escuela') ,x='Escuela', color = 'Escuela',)

    st.plotly_chart(fig5, use_container_width=True)



