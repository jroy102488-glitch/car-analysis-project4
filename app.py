import pandas as pd
import streamlit as st

import plotly.express as px

st.header('Dashboard de anúncios de carros')

car_data = pd.read_csv('vehicles_us.csv')

st.write('Visualização inicial dos dados')
st.write(car_data.head())

hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x='odometer', title='Distribuição da quilometragem')
    st.plotly_chart(fig, use_container_width=True)