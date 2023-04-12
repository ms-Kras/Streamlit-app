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
## Корреляция между размером общего счета и объемом чаевых
""")
st.write("""
Представленная на графике зависимость показывает, что с увеличением счета увеличивается и размер чаевых. 
Однако, мы так же можем отметить, что чаще всего чаевые оставляют при счете, не превышающем 20 долларов.
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.xlabel('Общий счет')
plt.ylabel('Чаевые')
st.pyplot(fig)

st.write("""
## Представление зависимости объема чаевых от размера общего счета и количества клиентов за столиком
""")
st.write("""
Анализ данных показал, что значительная доля чаевых была получена на заказах, предназначенных для двух персон. 
Вероятно, это связано с тем, что ресторан пользуется популярностью у гостей для проведения романтических встреч, деловых встреч и других подобных мероприятий. 
Рекомендуется провести дополнительное исследование данного факта, и при подтверждении гипотезы о популярности ресторана для такого типа встреч, 
разработать соответствующее меню, учитывающее потребности данной категории гостей.
""")

fig,ax=plt.subplots()
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='size', palette='coolwarm')
plt.xlabel('Общий счет')
plt.legend(title='Размер заказа', loc='upper left')
plt.ylabel('Чаевые')
st.pyplot(fig)

st.write("""
## Распределение объема выручки ресторана по дням недели
""")
st.write("""
Выходные дни имеют более высокий средний чек, в частности воскресенье. 
Воскресный график также отличается более высокими значениями чека и меньшим количеством маленьких заказов. 
В пятницу также заметна тенденция к увеличению размера чека, что делает этот день ближе к выходным в плане объема продаж.
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
