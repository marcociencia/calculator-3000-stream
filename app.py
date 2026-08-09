import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculator", page_icon="🪶")

# --- CSS Personalizado ---
st.markdown("""
    <style>
    /* Fundo geral da página */
    .stApp {
        background-color: #e5e5e5;
    }
    
    /* CORPO DA CALCULADORA */
    .block-container {
        background-color: #ffffff;
        max-width: 380px; 
        padding: 20px !important;
        margin-top: 5vh;
        border-radius: 12px;
        box-shadow: 
            0px 20px 30px rgba(0, 0, 0, 0.2), 
            0px 10px 10px rgba(0, 0, 0, 0.15),
            inset 0px -5px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #777;
    }

    /* --- BARRA DE TÍTULO FAKE (Estilo Windows) --- */
    .win-title-bar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: #ffffff;
        /* Estica a barra para ignorar o padding do corpo da calculadora */
        margin: -20px -20px 20px -20px; 
        padding: 10px 15px;
        border-top-left-radius: 11px;
        border-top-right-radius: 11px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #000;
        user-select: none;
    }
    .win-left {
        display: flex;
        align-items: center;
        gap: 8px;
        font-size: 13px;
    }
    .win-right {
        display: flex;
        align-items: center;
        gap: 15px;
        font-size: 14px;
        color: #333;
    }
    .win-right span {
        cursor: pointer;
        padding: 0 5px;
    }
    .win-right span:hover {
        color: #888;
    }
    .close-btn:hover {
        color: #e81123 !important; /* Vermelho padrão do Windows ao passar o mouse */
    }

    /* TELA DA CALCULADORA */
    .calc-display {
        background-color: #080707; /* Fundo preto solicitado originalmente */
        color: #ffffff;
        font-size: 45px;
        text-align: right;
        padding: 10px 15px;
        border-radius: 8px;
        margin-bottom: 20px;
        min-height: 80px;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0px 5px 10px rgba(0,0,0,0.8);
        overflow-x: auto;
    }

    /* --- ESTILO DOS BOTÕES 3D --- */
    div.stButton > button {
        width: 100%;
        height: 55px;
        border-radius: 8px;
        font-weight: bold !important;
        font-size: 20px !important;
        border: none !important;
        transition: all 0.1s ease;
        margin-bottom: 8px;
    }

    /* Botões Secundários (Números, C, CE) */
    div.stButton > button[kind="secondary"] {
        background-color: #383636 !important;
        color: white !important;
        box-shadow: 0px 5px 0px #1e1e1e, 0px 6px 8px rgba(0,0,0,0.3) !important; 
    }
    div.stButton > button[kind="secondary"]:active {
        transform: translateY(5px);
        box-shadow: 0px 0px 0px #1e1e1e, 0px 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    /* Botões Primários (Operações - Verde) */
    div.stButton > button[kind="primary"] {
        background-color: #4CAF50 !important; 
        color: white !important;
        box-shadow: 0px 5px 0px #2e7d32, 0px 6px 8px rgba(0,0,0,0.3) !important;
    }
    div.stButton > button[kind="primary"]:active {
        transform: translateY(5px);
        box-shadow: 0px 0px 0px #2e7d32, 0px 1px 2px rgba(0,0,0,0.3) !important;
    }
    
    /* Esconde barra superior nativa do Streamlit */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- INSERINDO A BARRA DE TÍTULO MOCK DO WINDOWS ---
st.markdown("""
<div class="win-title-bar">
    <div class="win-left">
        <span>🪶</span>
        <span>Calculadora</span>
    </div>
    <div class="win-right">
        <span>&#x2012;</span>
        <span>&#x25A1;</span>
        <span class="close-btn">&#x2715;</span>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Gerenciamento de Estado ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Funções ---
def add_to_calc(value):
    st.session_state.expression += str(value)

def clear_all():
    st.session_state.expression = ""

def clear_last():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate_result():
    try:
        result = str(eval(st.session_state.expression))
        st.session_state.expression = result
    except ZeroDivisionError:
        st.session_state.expression = "Erro: Div/0"
    except Exception:
        st.session_state.expression = "Erro"

# --- Interface: Tela ---
display_text = st.session_state.expression if st.session_state.expression != "" else "0"
st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

# --- Interface: Botões ---
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("CE", on_click=clear_last, use_container_width=True)
with col2: st.button("C", on_click=clear_all, use_container_width=True)
with col3: st.button("%", on_click=add_to_calc, args=("%",), use_container_width=True)
with col4: st.button("/", on_click=add_to_calc, args=("/",), type="primary", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
with col2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
with col3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
with col4: st.button("X", on_click=add_to_calc, args=("X",), type="primary", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1: st.button("4", on_click=add_to_calc, args=("4",), use_container_width=True)
with col2: st.button("5", on_click=add_to_calc, args=("5",), use_container_width=True)
with col3: st.button("6", on_click=add_to_calc, args=("6",), use_container_width=True)
with col4: st.button("-", on_click=add_to_calc, args=("-",), type="primary", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1: st.button("1", on_click=add_to_calc, args=("1",), use_container_width=True)
with col2: st.button("2", on_click=add_to_calc, args=("2",), use_container_width=True)
with col3: st.button("3", on_click=add_to_calc, args=("3",), use_container_width=True)
with col4: st.button("+", on_click=add_to_calc, args=("+",), type="primary", use_container_width=True)

col1, col2, col3 = st.columns([2, 1, 1])
with col1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
with col2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
with col3: st.button("=", on_click=calculate_result, type="primary", use_container_width=True)
