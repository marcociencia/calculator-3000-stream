import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Style Calculator 3000", page_icon="🧮", layout="centered")

# --- CSS Personalizado (para os botões ficarem redondos e bonitos) ---
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px;
        border-radius: 15px;
        background-color: #f8f9fa;
        border: 1px solid #ddd;
        transition: 0.2s;
    }
    .stButton > button:hover {
        background-color: #e2e6ea;
        border-color: #adb5bd;
        transform: scale(1.02);
    }
    .big-number {
        font-size: 48px !important;
        font-weight: bold !important;
        font-family: 'Courier New', monospace !important;
        text-align: right !important;
        padding-right: 20px;
    }
    .op-text {
        font-size: 30px;
        font-family: 'Courier New', monospace;
        padding-left: 5px;
    }
</style>
""", unsafe_allow_html=True)

# --- Inicialização do Estado (Session State) ---
if 'display' not in st.session_state:
    st.session_state.display = "0"       # O que aparece na tela grande principal
if 'first_num' not in st.session_state:
    st.session_state.first_num = ""      # Número primário
if 'operator' not in st.session_state:
    st.session_state.operator = ""       # Operador
if 'second_num' not in st.session_state:
    st.session_state.second_num = ""     # Número secundário
if 'result' not in st.session_state:
    st.session_state.result = ""         # Resultado final
if 'phase' not in st.session_state:
    st.session_state.phase = "primary"   # Fase atual: "primary" ou "secondary"

# --- Lógica dos Botões ---
def button_click(val):
    # 1. DIGITANDO NÚMEROS
    if val in "0123456789":
        if st.session_state.phase == "primary":
            if st.session_state.first_num == "0":
                st.session_state.first_num = val
            else:
                st.session_state.first_num += val
            st.session_state.display = st.session_state.first_num
        elif st.session_state.phase == "secondary":
            if st.session_state.second_num == "0":
                st.session_state.second_num = val
            else:
                st.session_state.second_num += val
            st.session_state.display = st.session_state.second_num

    # 2. OPERADORES (+, -, x)
    elif val in ["+", "-", "x"]:
        # Se já tem um número primário e não tem operador, registra o operador
        if st.session_state.first_num != "" and st.session_state.operator == "":
            st.session_state.operator = val
            st.session_state.phase = "secondary"
            st.session_state.display = val  # Mostra o operador na tela principal

    # 3. IGUAL (=)
    elif val == "=":
        if st.session_state.first_num != "" and st.session_state.operator != "" and st.session_state.second_num != "":
            n1 = int(st.session_state.first_num)
            n2 = int(st.session_state.second_num)
            
            if st.session_state.operator == "+":
                res = n1 + n2
            elif st.session_state.operator == "-":
                res = n1 - n2
            elif st.session_state.operator == "x":
                res = n1 * n2
            
            st.session_state.result = str(res)
            st.session_state.display = st.session_state.result
            st.session_state.phase = "primary"  # Reseta para permitir uma nova conta
            st.session_state.first_num = st.session_state.result
            st.session_state.second_num = ""
            st.session_state.operator = ""

    # 4. LIMPAR (C)
    elif val == "C":
        st.session_state.display = "0"
        st.session_state.first_num = ""
        st.session_state.operator = ""
        st.session_state.second_num = ""
        st.session_state.result = ""
        st.session_state.phase = "primary"

# --- INTERFACE VISUAL ---
st.title("🧮 Style Calculator 3000")

# 1. Tela de Exibição Principal (O Visor)
st.markdown(f"<div class='big-number'>{st.session_state.display}</div>", unsafe_allow_html=True)

# 2. O "Desenho" da linha quebrada (como na sua imagem)
# Isso fica abaixo da tela principal, para dar o efeito de "quebra de linha"
if st.session_state.operator != "":
    st.markdown("---") # Linha horizontal divisória
    
    col1, col2 = st.columns([1, 5])
    with col1:
        st.markdown(f"<div class='op-text'>{st.session_state.operator}</div>", unsafe_allow_html=True)
    with col2:
        # Exibe o número secundário ou um espaço vazio se ainda não foi digitado
        val_display = st.session_state.second_num if st.session_state.second_num != "" else "_"
        st.markdown(f"<div class='op-text' style='font-size: 40px;'>{val_display}</div>", unsafe_allow_html=True)
        
    if st.session_state.result != "":
        st.markdown("---") # Linha horizontal do resultado
        st.markdown(f"<div class='op-text' style='font-size: 40px; color: #2e7d32;'>RESULT: {st.session_state.result}</div>", unsafe_allow_html=True)

st.write("") # Espaço

# 3. Botões
# Linha 1
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("1"): button_click("1")
if c2.button("2"): button_click("2")
if c3.button("3"): button_click("3")
if c4.button("4"): button_click("4")
if c5.button("5"): button_click("5")

# Linha 2
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("6"): button_click("6")
if c2.button("7"): button_click("7")
if c3.button("8"): button_click("8")
if c4.button("9"): button_click("9")
if c5.button("0"): button_click("0")

# Linha 3 (Operadores e Ações)
c1, c2, c3, c4, c5 = st.columns(5)
if c1.button("+"): button_click("+")
if c2.button("-"): button_click("-")
if c3.button("x"): button_click("x")
if c4.button("="): button_click("=")
if c5.button("C"): button_click("C")
