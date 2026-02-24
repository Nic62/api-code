import streamlit as st
import pandas as pd
#df
df=pd.read_csv("database_log_todo.csv")
st.logo("logo.png")
#logo
col1, col2 = st.columns([6,1])

with col2:
    st.image("logo.png", width=120)
#paginas
st.page_link("site.py", label="Home", icon="📊")
st.page_link("pages/sitepesquisa.py", label="Pesquisa", icon="🔎")
st.page_link("pages/dashonline.py", label="Dashboard", icon="📈")
#titulo
st.markdown(
    "<h1 style='text-align: center;'>Dashboard</h1>",
    unsafe_allow_html=True
)
