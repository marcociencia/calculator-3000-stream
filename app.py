import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Calculadora Normal", page_icon="🧮", layout="centered")

# --- CSS para ficar bonito e parecer uma calculadora real ---
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 70px;
        font-size: 28px;
        border-radius: 12px;
        background-color: #f1f3f5;
        border: 1px solid #dee2e6;
        transition: 0.1s;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #e9ecef;
        border-color: #adb5bd;
        transform: scale(1.02);
    }
    .stButton > button:active {
        background-color: #ced4da;
    }
    /* Botão igual e operadores com cor diferente */
    .op-btn > button {
        background-color: #ffc107;
        border-color: #ffca3a;
    }
    .op-btn > button:hover {
        background-color: #ffca3a;
    }
    .eq-btn > button {
        background-color: #339af0;
        border-color: #339af0;
        color: white;
    }
    .eq-btn > button:hover {
        background-color: #228be6;
    }
    /* Visor da calculadora */
    .display-box {
        background-color: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 12px;
        padding: 20px 25px;
        font-size: 48px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        text-align: right;
        min-height: 90px;
        margin-bottom: 20px;
        overflow-x: auto;
        white-space: nowrap;
        box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# --- Inicialização do Estado (Session State) ---
if 'expression' not in st.session_state:
    st.session_state.expression = ""  # Guarda tudo que foi digitado (ex: "8+5")

# --- Lógica dos Botões ---
def button_click(val):
    current = st.session_state.expression

    # 1. SE APERTOU "=" (CALCULAR)
    if val == "=":
        try:
            # Substitui 'x' por '*' para o Python entender multiplicação
            calc_expression = current.replace("x", "*")
            # Calcula o resultado
            result = str(eval(calc_expression))
            st.session_state.expression = result
        except:
            st.session_state.expression = "Erro"

    # 2. SE APERTOU "C" (LIMPAR)
    elif val == "C":
        st.session_state.expression = ""

    # 3. SE APERTOU QUALQUER OUTRA COISA (números ou operadores)
    else:
        # Se a tela atual for "Erro" ou um resultado de conta anterior, começa do zero
        if current == "Erro" or (current != "" and current.replace("-","").replace("+","").replace("x","").replace("*","").isdigit() and val in "+-x*/"):
            st.session_state.expression = val
        else:
            st.session_state.expression += val

# --- INTERFACE DA CALCULADORA ---
st.title("🧮 Calculadora Padrão")

# Visor
st.markdown(f"<div class='display-box'>{st.session_state.expression if st.session_state.expression else '0'}</div>", unsafe_allow_html=True)

# Linha 1 (7, 8, 9, /, C)
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("7"): button_click("7")
if c2.button("8"): button_click("8")
if c3.button("9"): button_click("9")
with c4:
    st.markdown("<div class='op-btn'>", unsafe_allow_html=True)
    if st.button("/"): button_click("/")
    st.markdown("</div>", unsafe_allow_html=True)
if c5.button("C"): button_click("C")

# Linha 2 (4, 5, 6, x, -)
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("4"): button_click("4")
if c2.button("5"): button_click("5")
if c3.button("6"): button_click("6")
with c4:
    st.markdown("<div class='op-btn'>", unsafe_allow_html=True)
    if st.button("x"): button_click("x")
    st.markdown("</div>", unsafe_allow_html=True)
with c5:
    st.markdown("<div class='op-btn'>", unsafe_allow_html=True)
    if st.button("-"): button_click("-")
    st.markdown("</div>", unsafe_allow_html=True)

# Linha 3 (1, 2, 3, +, =)
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("1"): button_click("1")
if c2.button("2"): button_click("2")
if c3.button("3"): button_click("3")
with c4:
    st.markdown("<div class='op-btn'>", unsafe_allow_html=True)
    if st.button("+"): button_click("+")
    st.markdown("</div>", unsafe_allow_html=True)
with c5:
    st.markdown("<div class='eq-btn'>", unsafe_allow_html=True)
    if st.button("="): button_click("=")
    st.markdown("</div>", unsafe_allow_html=True)

# Linha 4 (0, ., 00)
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("0"): button_click("0")
if c2.button("."): button_click(".")
if c3.button("00"): button_click("00")
