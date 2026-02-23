import pandas as pd
import streamlit as st
#url
#Local URL: http://localhost:8501
# Network URL: http://192.168.1.1
#dados
df=pd.read_csv("database_log_todo.csv")
#logo
col1, col2 = st.columns([6,1])

with col2:
    st.image("logo.png", width=120)
#site
##titulo

st.markdown(
    "<h1 style='text-align: center;'>API CODE</h1>",
    unsafe_allow_html=True
)
st.dataframe(df)