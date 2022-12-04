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


st.title("Campus Administradores")




def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_hello = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_4vlxeulb.json")

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





boxes = {'Campus Administrador': ['Aguascalientes','Chihuahua','Ciudad de México','Ciudad Juárez','Cuernavaca','Cumbres','EGADE Monterrey','EGAP Monterrey','Estado de México','Eugenio Garza Lagüera','Eugenio Garza Sada','Guadalajara','Hidalgo','Irapuato','Laguna','León','Monterrey','Morelia','Puebla','Querétaro','San Luis Potosí','Santa Catarina','Santa Fe', 'Sonora Norte','Tampico','Tec de Monterrey','Toluca','Valle Alto','Zacatecas'],
        'QuantityInt': [6, 538, 576, 33, 283, 60, 76, 3, 480, 233, 614, 853, 252, 1, 75, 324, 1433, 106, 111, 326, 177, 401, 693, 76, 201, 2, 29, 50,16 ]
        
        }
dg = pd.DataFrame(boxes)

st.header('Campus con mayor impacto en Internacionalidad ☑')


fig2 = px.treemap(dg, path=["Campus Administrador"], values='QuantityInt', hover_name="Campus Administrador", color="QuantityInt")
st.plotly_chart(fig2, use_container_width=True)

