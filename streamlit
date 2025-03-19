import streamlit as st
import pandas as pd
import random

st.title("Прогноз задержки рейса S7-airlines")

st.sidebar.header("Вход в систему")
username = st.sidebar.text_input('Логин')
password = st.sidebar.text_input('Пароль', type  = 'password')
if st.sidebar.button("Войти"):
    st.sidebar.success(f"Добро пожаловать, {username}!")


st.subheader("База рейсов")



flights = pd.DataFrame({
    "Рейс": [f"S7 {random.randint(1000, 9999)}" for i in range(10)]})
flights.index= range(1,len(flights)+1)

st.dataframe(flights)

st.subheader("✈️ Информация о рейсе")
