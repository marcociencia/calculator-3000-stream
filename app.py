import streamlit as st

# Configuração da página (deve ser o primeiro comando)
st.set_page_config(page_title="Calculator", page_icon="🧮")

# --- CSS Personalizado para Layout, Tamanho Fixo e Efeito 3D ---
st.markdown("""
    <style>
    /* Fundo geral da página (cinza claro para destacar a calculadora branca) */
    .stApp {
        background-color: #e5e5e5;
    }
    
    /* 
       CORPO DA CALCULADORA:
       Define largura fixa, fundo branco, bordas arredondadas e sombra 3D 
    */
    .block-container {
        background-color: #ffffff;
        max-width: 400px; /* Comprimento fixo da calculadora */
        padding: 30px !important;
        margin-top: 5vh;
        border-radius: 20px;
        box-shadow: 
            0px 20px 30px rgba(0, 0, 0, 0.2), 
            0px 10px 10px rgba(0, 0, 0, 0.15),
            inset 0px -5px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #dcdcdc;
    }

    /* Tela da calculadora (Efeito afundado/LCD) */
    .calc-display {
        background-color: #1a1a1a;
        color: #ffffff;
        font-size: 45px;
        text-align: right;
        padding: 15px 20px;
        border-radius: 12px;
        margin-bottom: 25px;
        min-height: 85px;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0px 8px 10px rgba(0,0,0,0.6); /* Sombra interna para dar profundidade */
        border: 2px solid #333;
        overflow-x: auto;
    }

    /* Título da Calculadora */
    .calc-title {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
        color: #888;
        margin-bottom: 15px;
        font-size: 22px;
        letter-spacing: 2px;
    }

    /* --- ESTILO DOS BOTÕES (EFEITO FÍSICO 3D) --- */
    div.stButton > button {
        width: 100%;
        height: 60px;
        border-radius: 10px;
        font-weight: bold !important;
        font-size: 22px !important;
        border: none !important;
        transition: all 0.1s ease; /* Animação rápida */
        margin-bottom: 10px;
    }

    /* Botões Secundários (Números, C, CE) - Cinza Escuro */
    div.stButton > button[kind="secondary"] {
        background-color: #4a4a4a !important;
        color: white !important;
        /* Sombra grossa embaixo simulando altura do botão */
        box-shadow: 0px 6px 0px #2c2c2c, 0px 8px 10px rgba(0,0,0,0.3) !important; 
    }
    /* Efeito de Clique: Botão afunda */
    div.stButton > button[kind="secondary"]:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #2c2c2c, 0px 2px 3px rgba(0,0,0,0.3) !important;
    }
    
    /* Botões Primários (Operações) - Verde */
    div.stButton > button[kind="primary"] {
        background-color: #4CAF50 !important; 
        color: white !important;
        /* Sombra grossa embaixo simulando altura do botão */
        box-shadow: 0px 6px 0px #2e7d32, 0px 8px 10px rgba(0,0,0,0.3) !important;
    }
    /* Efeito de Clique: Botão afunda */
    div.stButton > button[kind="primary"]:active {
        transform: translateY(6px);
        box-shadow: 0px 0px 0px #2e7d32, 0px 2px 3px rgba(0,0,0,0.3) !important;
    }
    
    /* Remove botões padrões de UI do Streamlit do canto superior */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# Título estilizado da Calculadora
st.markdown('<div class="calc-title">CALCULATOR</div>', unsafe_allow_html=True)

# --- Gerenciamento de Estado (Memória da Calculadora) ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

# --- Funções da Calculadora ---
def add_to_calc(value):
    st.session_state.expression += str(value)

def clear_all():
    st.session_state.expression = ""

def clear_last():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate_result():
    try:
        # A função eval processa a string matemática
        result = str(eval(st.session_state.expression))
        st.session_state.expression = result
    except ZeroDivisionError:
        st.session_state.expression = "Erro: Div/0"
    except Exception:
        st.session_state.expression = "Erro"

# --- Interface: Tela ---
# Exibe a expressão ou "0" caso esteja vazia
display_text = st.session_state.expression if st.session_state.expression != "" else "0"
st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

# --- Interface: Botões ---
# Usamos st.columns para alinhar a grade de botões
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("CE", on_click=clear_last, use_container_width=True)
with col2: st.button("C", on_click=clear_all, use_container_width=True)
with col3: st.button("%", on_click=add_to_calc, args=("%",), use_container_width=True)
with col4: st.button("/", on_click=add_to_calc, args=("/",), type="primary", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
with col1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
with col2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
with col3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
with col4: st.button("X", on_click=add_to_calc, args=("*",), type="primary", use_container_width=True)

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

# O botão 0 ocupa um espaço equivalente a 2 colunas
col1, col2, col3 = st.columns([2, 1, 1])
with col1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
with col2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
with col3: st.button("=", on_click=calculate_result, type="primary", use_container_width=True)
