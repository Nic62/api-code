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
st.sidebar.title("Filtros")

modelo = st.sidebar.multiselect(
    "Selecione o Modelo",
    df["MODELO"].dropna().unique()
)

fornecedor = st.sidebar.multiselect(
    "Selecione o Fornecedor",
    df["FORNECEDOR"].dropna().unique()
)

estacao = st.sidebar.multiselect(
    "Selecione a Estação",
    df["ESTACAO"].dropna().unique()
)

# Aplicando filtros
df_filtrado = df.copy()

if modelo:
    df_filtrado = df_filtrado[df_filtrado["MODELO"].isin(modelo)]

if fornecedor:
    df_filtrado = df_filtrado[df_filtrado["FORNECEDOR"].isin(fornecedor)]

if estacao:
    df_filtrado = df_filtrado[df_filtrado["ESTACAO"].isin(estacao)]

# =========================
# KPIs
# =========================
st.title("📊 Dashboard Logístico")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total de Registros", len(df_filtrado))
col2.metric("Modelos Únicos", df_filtrado["MODELO"].nunique())
col3.metric("Fornecedores Únicos", df_filtrado["FORNECEDOR"].nunique())
col4.metric("Consumo Total", int(df_filtrado["CONSUMO"].sum()))

st.divider()

# =========================
# GRÁFICOS
# =========================

col1, col2 = st.columns(2)

# Consumo por Modelo
consumo_modelo = (
    df_filtrado.groupby("MODELO")["CONSUMO"]
    .sum()
    .reset_index()
    .sort_values(by="CONSUMO", ascending=False)
)

fig1 = px.bar(
    consumo_modelo,
    x="MODELO",
    y="CONSUMO",
    title="Consumo por Modelo"
)

col1.plotly_chart(fig1, use_container_width=True)

# Consumo por Estação
consumo_estacao = (
    df_filtrado.groupby("ESTACAO")["CONSUMO"]
    .sum()
    .reset_index()
    .sort_values(by="CONSUMO", ascending=False)
)

fig2 = px.bar(
    consumo_estacao,
    x="ESTACAO",
    y="CONSUMO",
    title="Consumo por Estação"
)

col2.plotly_chart(fig2, use_container_width=True)

# =========================
# TOP FORNECEDORES
# =========================

top_fornecedor = (
    df_filtrado.groupby("FORNECEDOR")["CONSUMO"]
    .sum()
    .reset_index()
    .sort_values(by="CONSUMO", ascending=False)
    .head(10)
)

fig3 = px.pie(
    top_fornecedor,
    names="FORNECEDOR",
    values="CONSUMO",
    title="Top 10 Fornecedores por Consumo"
)

st.plotly_chart(fig3, use_container_width=True)

# =========================
# TABELA DETALHADA
# =========================

st.subheader("Tabela Detalhada")

st.dataframe(df_filtrado, use_container_width=True)
