import streamlit as st
import pandas as pd
import random

st.title("Прогноз задержки рейса S7-airlines")

st.sidebar.header("Вход в систему")
username = st.sidebar.text_input('Логин')
password = st.sidebar.text_input('Пароль', type  = 'password')
if st.sidebar.button("Войти"):
    st.sidebar.success(f"Добро пожаловать, {username}!")

flights = pd.DataFrame({
    "Рейс": [f"S7 {random.randint(1000, 9999)}" for i in range(10)],
    "Откуда":[f".." for i in range(10)],
    "Куда":[f".." for i in range(10)],
    "Время вылета":[f".." for i in range(10)]})
flights.index= range(1,len(flights)+1)

tab1, tab2= st.tabs(["Главная","База рейсов"])

with tab2:
    st.subheader("База рейсов")
    st.dataframe(flights)

with tab1:
    st.subheader("Информация о рейсе")
    selected_flight = st.selectbox("Выберите рейс:", flights["Рейс"])
    flight_info = flights[flights["Рейс"] == selected_flight]
    st.write(f"**Маршрут:** ")
    st.write(f"**Время вылета:** ")
