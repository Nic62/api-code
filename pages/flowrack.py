import pandas as pd
import streamlit as st

# ======================
# DADOS
# ======================
df_fl = pd.read_excel(
    "FLOWRACKS CHANGAN - REV04.xlsm",
    engine="openpyxl"
)

df_geral = pd.read_csv(
    "database_log_todo.csv",
    encoding="latin1",
    sep=";",
    on_bad_lines="skip"
)

# ======================
# TRATAMENTO FLOWRACK
# ======================
linhas = []

for _, row in df_fl.iterrows():
    for end in str(row["ENDEREÇO"]).split("\n"):
        partes = [p.strip() for p in end.split("/")]

        if len(partes) >= 4:
            nova = row.copy()
            nova["Estação"] = partes[0]
            nova["Flowrack"] = partes[1]
            nova["Nível"] = partes[2]
            nova["Posição"] = partes[3]
            linhas.append(nova)

df_fl_tratado = pd.DataFrame(linhas)

df_fl_tratado = df_fl_tratado.drop(columns=["ENDEREÇO"])

# ======================
# CRIA CHAVE PARA JOIN (MUITO MAIS RÁPIDO)
# ======================
df_geral["key"] = (
    df_geral["CODIGO"].astype(str).str.strip() + "|" +
    df_geral["ESTACAO"].astype(str).str.strip()
)

df_geral_lookup = df_geral.set_index("key")["MODELO"].to_dict()

df_fl_tratado["key"] = (
    df_fl_tratado["PART NUMBER"].astype(str).str.strip() + "|" +
    df_fl_tratado["Estação"].astype(str).str.strip()
)

df_fl_tratado["MODELO"] = df_fl_tratado["key"].map(df_geral_lookup)

df_fl_tratado.drop(columns=["key"], inplace=True)

# ======================
# UI STREAMLIT
# ======================
st.page_link("site.py", label="Home", icon="📊")
st.page_link("pages/sitepesquisa.py", label="Pesquisa", icon="🔎")
st.page_link("pages/flowrack.py", label="Flowrack", icon="🔩")

st.dataframe(df_fl_tratado)
