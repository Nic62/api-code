import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# ======================
# DADOS
# ======================
@st.cache_data
def carregar_dados():
    return pd.read_csv(
        "database_log_todo.csv",
        encoding="latin1",
        sep=";",
        on_bad_lines="skip"
    )

df = carregar_dados()

df = df[df["CLASSIF"] != "OBSOLETO"]

df["CLASSIF"] = (
    df["CLASSIF"]
    .fillna("")
    .astype(str)
    .str.replace("_", " ", regex=False)
    .str.replace("+", "/", regex=False)
)

# ======================
# LOGO
# ======================
col1, col2 = st.columns([6, 1])

with col2:
    st.image("logo.png", width=120)

# ======================
# MENU
# ======================
st.page_link("site.py", label="Home", icon="📊")
st.page_link("pages/sitepesquisa.py", label="Pesquisa", icon="🔎")

# ======================
# TÍTULO
# ======================
st.markdown(
    "<h1 style='text-align:center;'>PESQUISA</h1>",
    unsafe_allow_html=True
)

# ======================
# SESSION STATE (ESSENCIAL)
# ======================
if "codigo" not in st.session_state:
    st.session_state.codigo = ""

# ======================
# INPUT (ÚNICA FONTE)
# ======================
termo = st.text_input(
    "Digite ou escaneie o código",
    key="codigo"
)

# botão scanner
abrir_scanner = st.button("📷 Ler QR Code")

# ======================
# SCANNER (APENAS VISUAL)
# ======================
if abrir_scanner:

    scanner_html = """
    <script src="https://unpkg.com/html5-qrcode"></script>

    <div id="reader" style="width:300px;"></div>

    <script>

    function onScanSuccess(decodedText) {
        // atualiza input direto no DOM (FUNCIONA)
        const input = window.parent.document.querySelector('input');

        if (input) {
            input.value = decodedText;
            input.dispatchEvent(new Event('input', { bubbles: true }));
        }
    }

    let scanner = new Html5QrcodeScanner("reader", {
        fps: 10,
        qrbox: 250,
        videoConstraints: {
            facingMode: "environment"
        }
    });

    scanner.render(onScanSuccess);

    </script>
    """

    components.html(scanner_html, height=400)

# ======================
# BUSCA (AGORA FUNCIONA)
# ======================
termo = st.session_state.codigo

if termo:

    resultados = df[
        df["CODIGO"]
        .astype(str)
        .str.contains(termo, case=False, na=False)
    ]

    col1, col2, col3 = st.columns([1, 2, 1])

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
