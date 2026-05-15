import streamlit as st
import pandas as pd

# dataframe
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "database_log_todo.csv",
        encoding="latin1",
        sep=";",
        on_bad_lines="skip"
    )

df = carregar_dados()

# filtro
df = df[df["CLASSIF"] != "OBSOLETO"]

df["CLASSIF"] = (
    df["CLASSIF"]
    .str.replace("_", " ", regex=False)
    .str.replace("+", "/", regex=False)
)

# logo
col1, col2 = st.columns([6,1])

with col2:
    st.image("logo.png", width=120)

# paginas
st.page_link("site.py", label="Home", icon="📊")
st.page_link("pages/sitepesquisa.py", label="Pesquisa", icon="🔎")

# titulo
st.markdown(
    "<h1 style='text-align: center;'>PESQUISA</h1>",
    unsafe_allow_html=True
)

# pesquisa
col1, col2, col3 = st.columns([1,2,1])

with col2:

    termo = st.text_input(
        "Digite ou escaneie o código",
        placeholder="Use leitor de código de barras"
    )

# resultado
if termo:

    resultados = df[
        df["CODIGO"]
        .astype(str)
        .str.contains(termo, case=False, na=False)
    ]

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        if not resultados.empty:

            for _, item in resultados.iterrows():

                with st.container(border=True):

                    st.subheader(item["CODIGO"])
                    st.subheader(item["MODELO"])
                    st.subheader(item["DESCRICAO"])
                    st.subheader(item["ESTACAO"])

                    st.write(item["CONSUMO"])
                    st.write(item["SUB_GRUPO_1"])
                    st.write(item["SUB_GRUPO_2"])
                    st.write(item["CLASSIF"])

        else:
            st.warning("Nenhum resultado encontrado.")
