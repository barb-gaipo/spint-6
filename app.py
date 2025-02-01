import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Datos de Vehículos")

# Cargar datos desde un archivo CSV (usa uno que tengas o descárgalo)
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón para mostrar un histograma
if st.button('Construir histograma'):
    st.write('Creación de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para mostrar un gráfico de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Creación de un gráfico de dispersión entre odómetro y precio')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
