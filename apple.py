import pandas as pd
import streamlit as st
import yfinance as yf

st.write("""
# Apple за последнее десятилетие

Данные о **цене закрытия акций** и **объеме торгов** компании Apple за период 01.04.2013-01.04.2023

""")
tickerSymbol='AAPL'
tickerData=yf.Ticker(tickerSymbol)
tickerDf=tickerData.history(period='1d', start ='2013-3-31', end='2023-3-31')

st.write("""
## Цена закрытия акций
""")
st.line_chart(tickerDf.Close)
st.write("""
## Объем торгов
""")
st.line_chart(tickerDf.Volume)