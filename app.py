import streamlit as st
import datetime as dt


st.write('aggiungere 2 ore a causa del fuso di heroku')
now = dt.datetime.now()
st.write(now)
