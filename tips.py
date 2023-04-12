import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns


path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
tips = pd.read_csv(path)
st.write("""
# Анализ данных ресторана
## Распределение счетов, чаевых и выручки по дням недели и времени обслуживания
""")
         
st.write("""
Представление общей выручки ресторана за изучаемый период
""")

fig,ax=plt.subplots()
sns.histplot(tips['total_bill'])
plt.xlabel('Общий счет')
plt.ylabel('Сумма')
st.pyplot(fig)

st.write("""
Корреляция между размером общего счета и объемом чаевых
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.xlabel('Общий счет')
plt.ylabel('Чаевые')
st.pyplot(fig)

st.write("""
Представление зависимости объема чаевых от размера общего счета и количества клиентов за столиком
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size', palette='coolwarm')
plt.xlabel('Общий счет')
plt.legend(title='Размер заказа', loc='upper left')
plt.ylabel('Чаевые')
st.pyplot(fig)

st.write("""
Распределение объема выручки ресторана по дням недели
""")

fig,ax=plt.subplots()
sns.boxplot(data=tips, x="day", y="total_bill")
plt.xlabel('День недели')
plt.ylabel('Общий счет')
st.pyplot(fig)

st.write("""
Зависимость объема чаевых от дня недели и пола посетителей ресторана
""")

fig,ax=plt.subplots()
sns.scatterplot(x='tip', y='day', size='tip', hue='sex', data=tips, palette={'Male': 'blue', 'Female': 'red'})
plt.xlabel('Чаевые')
plt.ylabel('День недели')
st.pyplot(fig)

st.write("""
Представление распределения общей суммы счетов за каждый день недели с учетом времени обслуживания
""")

fig,ax=plt.subplots()
sns.boxplot(data=tips, x='day', y='total_bill', hue='time')
plt.xlabel('День недели')
plt.ylabel('Общий счет')
st.pyplot(fig)
