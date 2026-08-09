import streamlit as st

# --- Configuração ---
st.set_page_config(page_title="Calculadora Retrô", page_icon="🧮", layout="centered")

# --- CSS (Recriando o visual Tkinter, pois webview não roda na nuvem) ---
st.markdown("""
<style>
    /* Fundo clássico */
    .stApp {
        background-color: #d4d0c8; 
    }
    
    /* Container da calculadora */
    .calc-window {
        background-color: #d4d0c8;
        padding: 20px;
        border: 2px solid #ffffff;
        border-right-color: #808080;
        border-bottom-color: #808080;
        max-width: 400px;
        margin: 0 auto;
        border-radius: 4px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    }

    /* Visor (Display) */
    .display-box {
        background-color: white;
        border: 3px inset #808080;
        padding: 15px;
        font-size: 32px;
        font-family: 'Courier New', monospace;
        text-align: right;
        margin-bottom: 15px;
        min-height: 55px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
        color: black;
    }

    /* Botões estilo 3D igual Tkinter */
    .win-btn {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
        border: 2px solid #ffffff;
        border-right-color: #404040;
        border-bottom-color: #404040;
        background-color: #dcdcdc; /* gainsboro */
        cursor: pointer;
        color: black;
        transition: 0.05s;
    }
    .win-btn:active {
        border: 2px solid #404040;
        border-right-color: #ffffff;
        border-bottom-color: #ffffff;
        transform: translate(2px, 2px);
    }

    /* Cores personalizadas do seu Tkinter original */
    .btn-num { background-color: #dcdcdc; }
    .btn-op  { background-color: #008000; color: white; }
    .btn-dot { background-color: #FFA500; color: white; }
    .btn-clear { background-color: #FF0000; color: white; }
    .btn-equal { background-color: #FFD700; color: black; }
</style>
""", unsafe_allow_html=True)

# --- Lógica Matemática (igual ao Tkinter) ---
if 'expressao' not in st.session_state:
    st.session_state.expressao = ""

def press(num):
    st.session_state.expressao += str(num)

def limpar():
    st.session_state.expressao = ""

def teclaigual():
    try:
        # Substitui visualmente para o eval entender
        calc = st.session_state.expressao.replace('x', '*').replace('÷', '/')
        total = str(eval(calc))
        st.session_state.expressao = total
    except:
        st.session_state.expressao = " error "

# --- Layout no Streamlit usando colunas ---
st.markdown('<div class="calc-window">', unsafe_allow_html=True)

# Visor
st.markdown(f'<div class="display-box">{st.session_state.expressao if st.session_state.expressao else ""}</div>', unsafe_allow_html=True)

# Layout de Botões (4 colunas normais + 1 coluna extra para o "=")
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 0.7])

# Linha 1 (7, 8, 9, +)
with col1:
    if st.button("7", key="b7"): press(7)
with col2:
    if st.button("8", key="b8"): press(8)
with col3:
    if st.button("9", key="b9"): press(9)
with col4:
    st.markdown('<div class="btn-op">', unsafe_allow_html=True)
    if st.button("+", key="b+"): press("+")
    st.markdown('</div>', unsafe_allow_html=True)
with col5:
    # Botão = ocupa altura total
    if st.button("=", key="b="): teclaigual()

# Linha 2 (4, 5, 6, -)
with col1:
    if st.button("4", key="b4"): press(4)
with col2:
    if st.button("5", key="b5"): press(5)
with col3:
    if st.button("6", key="b6"): press(6)
with col4:
    st.markdown('<div class="btn-op">', unsafe_allow_html=True)
    if st.button("-", key="b-"): press("-")
    st.markdown('</div>', unsafe_allow_html=True)
with col5:
    st.write("") # Espaço para manter a coluna 5 alinhada

# Linha 3 (1, 2, 3, /)
with col1:
    if st.button("1", key="b1"): press(1)
with col2:
    if st.button("2", key="b2"): press(2)
with col3:
    if st.button("3", key="b3"): press(3)
with col4:
    st.markdown('<div class="btn-op">', unsafe_allow_html=True)
    if st.button("/", key="b/"): press("/")
    st.markdown('</div>', unsafe_allow_html=True)
with col5:
    st.write("") # Espaço

# Linha 4 (0, ., C, x)
with col1:
    if st.button("0", key="b0"): press(0)
with col2:
    st.markdown('<div class="btn-dot">', unsafe_allow_html=True)
    if st.button(".", key="b."): press(".")
    st.markdown('</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="btn-clear">', unsafe_allow_html=True)
    if st.button("C", key="bC"): limpar()
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="btn-op">', unsafe_allow_html=True)
    if st.button("x", key="bx"): press("*")
    st.markdown('</div>', unsafe_allow_html=True)
with col5:
    st.write("") # Espaço

st.markdown('</div>', unsafe_allow_html=True)
