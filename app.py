import pandas as pd
import streamlit as st
import plotly.express as px

# Cabeçalho
st.header("Dashboard de anúncios de carros")

# Ler os dados
car_data = pd.read_csv("vehicles_us.csv")

# Visualização inicial
st.write("Visualização inicial dos dados")
st.dataframe(car_data.head())

# Botão para histograma
hist_button = st.button("Criar histograma")

if hist_button:
    st.write("Criando um histograma para o conjunto de dados de anúncios de vendas de carros")
    fig_hist = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da quilometragem"
    )
    st.plotly_chart(fig_hist, use_container_width=True)

# Checkbox para gráfico de dispersão
show_scatter = st.checkbox("Mostrar gráfico de dispersão")

if show_scatter:
    st.write("Criando um gráfico de dispersão entre preço e quilometragem")
    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Preço vs Quilometragem"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)