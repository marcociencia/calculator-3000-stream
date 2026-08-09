import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculator", page_icon="🧮")

# --- CSS Personalizado para Cores e Layout ---
st.markdown("""
    <style>
    /* Muda a cor de fundo do aplicativo (calculadora) para cinza */
    .stApp {
        background-color: #6c6c6c;
    }
    
    /* Tela da calculadora */
    .calc-display {
        background-color: #1e1e1e;
        color: white;
        font-size: 40px;
        text-align: right;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        min-height: 90px;
        font-family: monospace;
        box-shadow: inset 0px 0px 10px rgba(0,0,0,0.5);
    }

    /* Estilo dos botões secundários (Números, C, CE, %) */
    div.stButton > button[kind="secondary"] {
        background-color: #383636 !important;
        color: white !important;
        font-size: 24px !important;
        height: 60px;
        border: none;
    }
    div.stButton > button[kind="secondary"]:hover {
        background-color: #505050 !important;
    }
    
    /* Estilo dos botões primários (Operadores: /, X, -, +, =) - MUDADO PARA VERDE */
    div.stButton > button[kind="primary"] {
        background-color: #4CAF50 !important; /* Verde */
        color: white !important;
        font-size: 24px !important;
        height: 60px;
        border: none !important;
    }
    div.stButton > button[kind="primary"]:hover {
        background-color: #45a049 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Título atualizado
st.title("Calculator")

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
# Usamos um componente markdown HTML para a tela replicar o visual preto antigo
display_text = st.session_state.expression if st.session_state.expression != "" else "0"
st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

# --- Interface: Botões ---
# Linha 1: CE, C, %, /
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("CE", on_click=clear_last, use_container_width=True)
with col2: st.button("C", on_click=clear_all, use_container_width=True)
with col3: st.button("%", on_click=add_to_calc, args=("%",), use_container_width=True)
with col4: st.button("/", on_click=add_to_calc, args=("/",), type="primary", use_container_width=True)

# Linha 2: 7, 8, 9, X
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
with col2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
with col3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
with col4: st.button("X", on_click=add_to_calc, args=("*",), type="primary", use_container_width=True)

# Linha 3: 4, 5, 6, -
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("4", on_click=add_to_calc, args=("4",), use_container_width=True)
with col2: st.button("5", on_click=add_to_calc, args=("5",), use_container_width=True)
with col3: st.button("6", on_click=add_to_calc, args=("6",), use_container_width=True)
with col4: st.button("-", on_click=add_to_calc, args=("-",), type="primary", use_container_width=True)

# Linha 4: 1, 2, 3, +
col1, col2, col3, col4 = st.columns(4)
with col1: st.button("1", on_click=add_to_calc, args=("1",), use_container_width=True)
with col2: st.button("2", on_click=add_to_calc, args=("2",), use_container_width=True)
with col3: st.button("3", on_click=add_to_calc, args=("3",), use_container_width=True)
with col4: st.button("+", on_click=add_to_calc, args=("+",), type="primary", use_container_width=True)

# Linha 5: 0 (largo), ., =
# Definimos pesos para as colunas para que o 0 ocupe o espaço de 2 botões como no Tkinter
col1, col2, col3 = st.columns([2, 1, 1])
with col1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
with col2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
with col3: st.button("=", on_click=calculate_result, type="primary", use_container_width=True)
