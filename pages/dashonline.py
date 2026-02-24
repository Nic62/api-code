import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# =========================
# LOAD CSV
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv(
        "database_log_todo.csv",
        sep=";",
        decimal=",",
        thousands=".",
        encoding="latin1"
    )
    
    # Garantindo que CONSUMO seja numérico
    df["CONSUMO"] = pd.to_numeric(df["CONSUMO"], errors="coerce")
    df["CONSUMO"] = df["CONSUMO"].fillna(0)

    return df

df = load_data()

# =========================
# FILTROS
# =========================
st.sidebar.title("Filtros")

modelo = st.sidebar.multiselect(
    "Selecione o Modelo",
    sorted(df["MODELO"].dropna().unique())
)

estacao = st.sidebar.multiselect(
    "Selecione a Estação",
    sorted(df["ESTACAO"].dropna().unique())
)

df_filtrado = df.copy()

if modelo:
    df_filtrado = df_filtrado[df_filtrado["MODELO"].isin(modelo)]

if estacao:
    df_filtrado = df_filtrado[df_filtrado["ESTACAO"].isin(estacao)]

# =========================
# KPIs
# =========================
st.title("📊 Dashboard Logístico")

col1, col2, col3 = st.columns(3)

col1.metric("Total Registros", len(df_filtrado))
col2.metric("Consumo Total", f"{df_filtrado['CONSUMO'].sum():,.0f}")
col3.metric("Média Consumo", f"{df_filtrado['CONSUMO'].mean():,.2f}")

st.divider()

# =========================
# BOXPLOT POR MODELO
# =========================
st.subheader("Distribuição de Consumo por Modelo")

fig1 = px.box(
    df_filtrado,
    x="MODELO",
    y="CONSUMO",
    points="outliers",  # mostra outliers
    title="Boxplot - Consumo por Modelo"
)

st.plotly_chart(fig1, use_container_width=True)

# =========================
# BOXPLOT POR ESTAÇÃO
# =========================
st.subheader("Distribuição de Consumo por Estação")

fig2 = px.box(
    df_filtrado,
    x="ESTACAO",
    y="CONSUMO",
    points="outliers",
    title="Boxplot - Consumo por Estação"
)

st.plotly_chart(fig2, use_container_width=True)

# =========================
# TABELA
# =========================
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado, use_container_width=True)
