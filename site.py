import pandas as pd
import streamlit as st

df = pd.read_csv("database_log_todo.csv",encoding="latin1", sep=",")
col1, col2 = st.columns([6,1])

with col2:
    st.image("logo.png", width=120)
st.page_link("site.py", label="Home", icon="📊")
st.page_link("pages/sitepesquisa.py", label="Pesquisa", icon="🔎")

st.markdown(
    "<h1 style='text-align: center;'>API CODE</h1>",
    unsafe_allow_html=True
)
st.dataframe(df)
