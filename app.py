import streamlit as st

# --- Configuração da Página ---
st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# --- CSS Personalizado (Recriando o visual do Tkinter com as cores exatas) ---
st.markdown("""
<style>
    /* Fundo cinza claro como a janela do Tkinter */
    .stApp {
        background-color: #d4d0c8; 
    }
    
    /* Container para centralizar e dar o aspecto de janela */
    .calc-window {
        background-color: #d4d0c8;
        padding: 20px;
        border: 2px solid #ffffff;
        border-right-color: #808080;
        border-bottom-color: #808080;
        max-width: 400px;
        margin: 0 auto;
        border-radius: 5px;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
    }

    /* Visor (Igual ao Entry do Tkinter) */
    .display-box {
        background-color: white;
        border: 3px inset #808080;
        padding: 15px;
        font-size: 30px;
        font-family: 'Verdana', sans-serif;
        text-align: right;
        margin-bottom: 20px;
        min-height: 60px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
        color: black;
    }

    /* Estilo base dos botões (3D igual ao Tkinter) */
    .win-btn {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-family: 'Verdana', sans-serif;
        border: 2px solid #ffffff;
        border-right-color: #404040;
        border-bottom-color: #404040;
        background-color: #dcdcdc; /* Gainsboro */
        cursor: pointer;
        transition: 0.05s;
        font-weight: bold;
    }
    .win-btn:active {
        border: 2px solid #404040;
        border-right-color: #ffffff;
        border-bottom-color: #ffffff;
        transform: translate(1px, 1px);
    }

    /* Cores customizadas do seu código Tkinter */
    .btn-num { background-color: #dcdcdc; } /* gainsboro */
    .btn-op  { background-color: #008000; color: white; } /* green */
    .btn-dot { background-color: #FFA500; color: white; } /* orange */
    .btn-clear { background-color: #FF0000; color: white; } /* red */
    .btn-equal { background-color: #FFD700; color: black; } /* Gold */
</style>
""", unsafe_allow_html=True)

# --- Lógica da Calculadora (mesma do seu código Tkinter) ---
if 'expressao' not in st.session_state:
    st.session_state.expressao = ""

def press(num):
    st.session_state.expressao += str(num)

def limpar():
    st.session_state.expressao = ""

def teclaigual():
    try:
        total = str(eval(st.session_state.expressao))
        st.session_state.expressao = total
    except:
        st.session_state.expressao = " error "

# --- Renderização do HTML (Para replicar o Grid exato) ---
st.markdown('<div class="calc-window">', unsafe_allow_html=True)

# 1. Visor
st.markdown(f'<div class="display-box">{st.session_state.expressao if st.session_state.expressao else ""}</div>', unsafe_allow_html=True)

# 2. Botões (Mapeados exatamente pelo seu código Tkinter)
# Usamos um Grid CSS para alinhar perfeitamente os 4x4 botões
grid_html = """
<div style="display: grid; grid-template-columns: repeat(4, 1fr) 60px; gap: 8px;">
    
    <!-- Linha 1 -->
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '7'}, '*')">7</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '8'}, '*')">8</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '9'}, '*')">9</button>
    <button class="win-btn btn-op" onclick="parent.postMessage({value: '+'}, '*')">+</button>
    
    <!-- Botão = Gigante ocupando 4 linhas (Coluna extra) -->
    <button class="win-btn btn-equal" style="grid-row: span 4; height: 100%;" onclick="parent.postMessage({value: '='}, '*')">=</button>

    <!-- Linha 2 -->
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '4'}, '*')">4</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '5'}, '*')">5</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '6'}, '*')">6</button>
    <button class="win-btn btn-op" onclick="parent.postMessage({value: '-'}, '*')">-</button>

    <!-- Linha 3 -->
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '1'}, '*')">1</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '2'}, '*')">2</button>
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '3'}, '*')">3</button>
    <button class="win-btn btn-op" onclick="parent.postMessage({value: '/'}, '*')">/</button>

    <!-- Linha 4 -->
    <button class="win-btn btn-num" onclick="parent.postMessage({value: '0'}, '*')">0</button>
    <button class="win-btn btn-dot" onclick="parent.postMessage({value: '.'}, '*')">.</button>
    <button class="win-btn btn-clear" onclick="parent.postMessage({value: 'C'}, '*')">C</button>
    <button class="win-btn btn-op" onclick="parent.postMessage({value: '*'}, '*')">*</button>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Captura os cliques dos botões HTML e chama as funções Python ---
# (Isso é necessário porque o Streamlit bloqueia o onclick padrão)
if 'clicked_value' not in st.session_state:
    st.session_state.clicked_value = None

clicked = st.query_params.get("value")
if clicked:
    # Limpa o parâmetro da URL para evitar múltiplas execuções
    st.query_params.clear()
    
    val = str(clicked)
    if val == "=":
        teclaigual()
    elif val == "C":
        limpar()
    else:
        press(val)
    st.rerun()
