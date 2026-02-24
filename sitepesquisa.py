import streamlit as st
import pandas as pd
#df
df=pd.read_csv("database_log_todo.csv")
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
    "<h1 style='text-align: center;'>PESQUISA</h1>",
    unsafe_allow_html=True
)
#pesquisa
col1, col2, col3 = st.columns([1,2,1])

with col2:
    termo = st.text_input("Digite o código para pesquisa")
#resposta
if termo:
    resultados = df[df["CODIGO"].astype(str).str.lower().str.contains(termo.lower())]

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if not resultados.empty:
            for _, item in resultados.iterrows():
                with st.container(border=True):
                    st.subheader(item["CODIGO"])
                    st.subheader(item["ESTACAO"])
                    st.write(item["SUB_GRUPO_1"])
                    st.write(item["SUB_GRUPO_2"])
                    st.write(item["CLASSIF"])
        else:
            st.warning("Nenhum resultado encontrado.")