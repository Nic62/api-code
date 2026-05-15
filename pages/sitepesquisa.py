import streamlit as st
import streamlit.components.v1 as components

st.title("Scanner QR Code")

codigo = st.text_input("Código recebido do scanner")

scanner_html = """
<script src="https://unpkg.com/html5-qrcode"></script>

<div id="reader" style="width:300px;"></div>

<script>
function onScanSuccess(decodedText) {
    const input = window.parent.document.querySelector('input');
    if (input) {
        input.value = decodedText;
        input.dispatchEvent(new Event('input', { bubbles: true }));
    }
}

let html5QrcodeScanner = new Html5QrcodeScanner(
    "reader",
    { fps: 10, qrbox: 250 }
);

html5QrcodeScanner.render(onScanSuccess);
</script>
"""

components.html(scanner_html, height=400)

st.write("Resultado:", codigo)
