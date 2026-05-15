import streamlit as st
import pandas as pd
from streamlit_qrcode_scanner import qrcode_scanner

# df
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "database_log_todo.csv",
        encoding="latin1",
        sep=";",
        on_bad_lines="skip"
    )

df = carregar_dados()

# título
st.title("PESQUISA")

# 🔥 SCANNER DE CÂMERA
codigo_qr = qrcode_scanner("Abra a câmera para escanear")

# fallback manual
termo = st.text_input("Ou digite o código")

# se veio do QR
if codigo_qr:
    termo = codigo_qr
    st.success(f"Escaneado: {termo}")

# busca
if termo:
    resultados = df[df["CODIGO"].astype(str).str.contains(termo, case=False, na=False)]

    if not resultados.empty:
        st.dataframe(resultados)
    else:
        st.warning("Nenhum resultado encontrado")
