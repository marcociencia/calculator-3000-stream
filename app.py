import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculator", page_icon="🪶")

# --- GERENCIAMENTO DE ESTADO ---
# Memória dos números digitados
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Controle da Janela (normal, max, min, closed)
if "win_state" not in st.session_state:
    st.session_state.win_state = "normal"

# --- FUNÇÕES DA CALCULADORA ---
def add_to_calc(value):
    st.session_state.expression += str(value)

def clear_all():
    st.session_state.expression = ""

def clear_last():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate_result():
    try:
        # Pulo do gato: substitui o 'x' (visual) por '*' (matemático) antes de calcular
        expr = st.session_state.expression.replace("x", "*")
        result = str(eval(expr))
        st.session_state.expression = result
    except ZeroDivisionError:
        st.session_state.expression = "Erro: Div/0"
    except Exception:
        st.session_state.expression = "Erro"

def set_win_state(new_state):
    # Se clicar em maximizar quando já estiver maximizado, ele restaura (normal)
    if st.session_state.win_state == new_state and new_state == "max":
        st.session_state.win_state = "normal"
    else:
        st.session_state.win_state = new_state

# --- ESTADO: FECHADO ---
# Se a janela for fechada, oculta a calculadora e exibe um botão de reabrir
if st.session_state.win_state == "closed":
    st.warning("A calculadora foi fechada.")
    st.button("Abrir Calculadora", on_click=set_win_state, args=("normal",))
    st.stop() # Interrompe a execução do restante da tela

# --- LÓGICA DE ZOOM (Largura Dinâmica) ---
# Se o estado for "max" (maximizado), aplica o zoom aumentando a largura
max_width = "700px" if st.session_state.win_state == "max" else "380px"

# --- CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #e5e5e5;
    }}
    
    /* CORPO DA CALCULADORA */
    .block-container {{
        background-color: #ffffff;
        max-width: {max_width}; /* Controlado pelo Python via Zoom */
        padding: 15px 20px 20px 20px !important;
        margin-top: 5vh;
        border-radius: 12px;
        box-shadow: 
            0px 20px 30px rgba(0, 0, 0, 0.2), 
            0px 10px 10px rgba(0, 0, 0, 0.15),
            inset 0px -5px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #777;
        transition: max-width 0.3s ease-in-out; /* Animação suave no zoom */
    }}

    /* TELA DA CALCULADORA */
    .calc-display {{
        background-color: #080707;
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
    }}

    /* --- ESTILO DOS BOTÕES DA CALCULADORA (3D) --- */
    div.stButton > button {{
        width: 100%;
        height: 55px;
        border-radius: 8px;
        font-weight: bold !important;
        font-size: 20px !important;
        border: none !important;
        transition: all 0.1s ease;
        margin-bottom: 8px;
    }}

    div.stButton > button[kind="secondary"] {{
        background-color: #383636 !important;
        color: white !important;
        box-shadow: 0px 5px 0px #1e1e1e, 0px 6px 8px rgba(0,0,0,0.3) !important; 
    }}
    div.stButton > button[kind="secondary"]:active {{
        transform: translateY(5px);
        box-shadow: 0px 0px 0px #1e1e1e, 0px 1px 2px rgba(0,0,0,0.3) !important;
    }}
    
    div.stButton > button[kind="primary"] {{
        background-color: #4CAF50 !important; 
        color: white !important;
        box-shadow: 0px 5px 0px #2e7d32, 0px 6px 8px rgba(0,0,0,0.3) !important;
    }}
    div.stButton > button[kind="primary"]:active {{
        transform: translateY(5px);
        box-shadow: 0px 0px 0px #2e7d32, 0px 1px 2px rgba(0,0,0,0.3) !important;
    }}

    /* --- ESTILO ESPECÍFICO DOS BOTÕES DA BARRA DE TAREFAS --- 
       Usamos o atributo 'title' (help) gerado pelo Streamlit para formatá-los 
       como ícones de janelas nativas, ignorando o estilo 3D acima. 
    */
    button[title="Minimize"], button[title="Maximize"], button[title="Close"] {{
        background-color: transparent !important;
        color: #000 !important;
        box-shadow: none !important;
        border-radius: 0px !important;
        height: 40px !important;
        font-size: 16px !important;
        padding: 0px !important;
        margin-top: -10px !important;
        transform: none !important;
    }}
    button[title="Minimize"]:hover, button[title="Maximize"]:hover {{
        background-color: #e5e5e5 !important;
    }}
    button[title="Close"]:hover {{
        background-color: #e81123 !important;
        color: white !important;
    }}
    
    /* Esconde barra superior nativa do Streamlit */
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- BARRA DE TÍTULO (Com controles funcionais) ---
col_icon, col_min, col_max, col_close = st.columns([7.5, 1, 1, 1])
with col_icon: 
    # Título
    st.markdown("<div style='font-size: 14px; font-weight: 500; font-family: sans-serif;'><span style='margin-right: 5px;'>🪶</span> Calculadora</div>", unsafe_allow_html=True)
with col_min: 
    # Botão Minimizar
    st.button("—", key="btn_min", help="Minimize", on_click=set_win_state, args=("min",), use_container_width=True)
with col_max: 
    # Botão Maximizar (Zoom)
    st.button("□", key="btn_max", help="Maximize", on_click=set_win_state, args=("max",), use_container_width=True)
with col_close: 
    # Botão Fechar
    st.button("✕", key="btn_close", help="Close", on_click=set_win_state, args=("closed",), use_container_width=True)


# --- CORPO DA CALCULADORA (Oculto se Minimizada) ---
if st.session_state.win_state != "min":
    # Espaçamento para descolar da barra superior
    st.write("") 

    # Interface: Tela
    display_text = st.session_state.expression if st.session_state.expression != "" else "0"
    st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

    # Interface: Botões (Linha 1)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("CE", on_click=clear_last, use_container_width=True)
    with col2: st.button("C", on_click=clear_all, use_container_width=True)
    with col3: st.button("%", on_click=add_to_calc, args=("%",), use_container_width=True)
    with col4: st.button("/", on_click=add_to_calc, args=("/",), type="primary", use_container_width=True)

    # Interface: Botões (Linha 2)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
    with col2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
    with col3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
    # AQUI: Mudamos para 'x' visualmente
    with col4: st.button("x", on_click=add_to_calc, args=("x",), type="primary", use_container_width=True)

    # Interface: Botões (Linha 3)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("4", on_click=add_to_calc, args=("4",), use_container_width=True)
    with col2: st.button("5", on_click=add_to_calc, args=("5",), use_container_width=True)
    with col3: st.button("6", on_click=add_to_calc, args=("6",), use_container_width=True)
    with col4: st.button("-", on_click=add_to_calc, args=("-",), type="primary", use_container_width=True)

    # Interface: Botões (Linha 4)
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("1", on_click=add_to_calc, args=("1",), use_container_width=True)
    with col2: st.button("2", on_click=add_to_calc, args=("2",), use_container_width=True)
    with col3: st.button("3", on_click=add_to_calc, args=("3",), use_container_width=True)
    with col4: st.button("+", on_click=add_to_calc, args=("+",), type="primary", use_container_width=True)

    # Interface: Botões (Linha 5)
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
    with col2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
    with col3: st.button("=", on_click=calculate_result, type="primary", use_container_width=True)
