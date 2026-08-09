import streamlit as st

# --- Configuração ---
st.set_page_config(page_title="Calculadora Retrô", page_icon="🖥️", layout="centered")

# --- CSS e HTML Customizado (Para imitar o visual 3D da imagem) ---
# Isso cria os botões, o visor e o layout exato da sua imagem
st.markdown("""
<style>
    /* Reset básico */
    .stApp {
        background-color: #d4d0c8; /* Cinza clássico Windows 95 */
    }
    
    /* Container principal que simula a janela */
    .calc-container {
        background-color: #c0c0c0;
        padding: 20px;
        border-radius: 8px;
        box-shadow: inset -2px -2px 5px #808080, inset 2px 2px 5px #ffffff;
        max-width: 400px;
        margin: 0 auto;
        border: 2px solid #ffffff;
        border-right-color: #808080;
        border-bottom-color: #808080;
    }

    /* Visor LCD 3D */
    .display-box {
        background-color: #ffffff;
        border: 2px solid #808080;
        border-top-color: #404040;
        border-left-color: #404040;
        padding: 15px 20px;
        font-size: 36px;
        font-family: 'Courier New', monospace;
        text-align: right;
        margin-bottom: 20px;
        box-shadow: inset 2px 2px 3px rgba(0,0,0,0.2);
        color: #000;
        height: 70px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
    }

    /* Botões estilo Windows 95 (3D Bevel) */
    .win-btn {
        width: 100%;
        height: 60px;
        font-size: 22px;
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
        background-color: #d4d0c8;
        border: 2px solid #ffffff;
        border-right-color: #404040;
        border-bottom-color: #404040;
        cursor: pointer;
        transition: 0.1s;
        color: black;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: none;
        border-radius: 0; /* Botões quadrados */
    }
    
    /* Efeito de clique (afunda o botão) */
    .win-btn:active {
        border: 2px solid #404040;
        border-right-color: #ffffff;
        border-bottom-color: #ffffff;
        transform: translate(2px, 2px);
    }

    /* Cores específicas baseadas na imagem */
    .btn-num { background-color: #d4d0c8; } /* Botões cinza claro */
    .btn-op { background-color: #008000; color: white; } /* Botões verdes */
    .btn-dot { background-color: #FFA500; color: white; } /* Botão laranja (.) */
    .btn-clear { background-color: #FF0000; color: white; } /* Botão vermelho (C) */
    .btn-equal { 
        background-color: #FFD700; 
        color: black;
        height: 100%; /* Ocupa toda a altura disponível na grade */
    }

    /* Layout de Grade 4x4 (para empilhar os botões) */
    .grid-calc {
        display: grid;
        grid-template-columns: repeat(4, 1fr) 60px; /* 4 colunas normais + 1 coluna estreita pro '=' */
        gap: 8px;
    }
    
    /* O botão '=' ocupa 4 linhas na grade */
    .span-4-rows {
        grid-row: span 4;
    }
</style>
""", unsafe_allow_html=True)

# --- Estado da Calculadora ---
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# --- Função de Clique ---
def button_click(val):
    current = st.session_state.expression

    if val == "=":
        try:
            calc_expression = current.replace("x", "*").replace("÷", "/")
            result = str(eval(calc_expression))
            st.session_state.expression = result
        except:
            st.session_state.expression = "Erro"
    elif val == "C":
        st.session_state.expression = ""
    else:
        if current == "Erro" or (current != "" and current.replace("-","").replace("+","").replace("x","").replace("÷","").replace("*","").replace("/","").isdigit() and val in "+-x÷*/"):
            st.session_state.expression = val
        else:
            st.session_state.expression += val

# --- Interface Visual (Usando HTML direto) ---
st.markdown('<div class="calc-container">', unsafe_allow_html=True)

# Visor
st.markdown(f'<div class="display-box">{st.session_state.expression if st.session_state.expression else ""}</div>', unsafe_allow_html=True)

# Grid de Botões (HTML Mapeado 1:1 com a imagem)
# A string HTML é construída e renderizada. O Streamlit não interfere nos botões HTML.
grid_html = """
<div class="grid-calc">
    <!-- Linha 1 -->
    <button class="win-btn btn-num" onclick="parent.postMessage('7', '*')">7</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('8', '*')">8</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('9', '*')">9</button>
    <button class="win-btn btn-op" onclick="parent.postMessage('+', '*')">+</button>
    <button class="win-btn btn-equal span-4-rows" onclick="parent.postMessage('=', '*')">=</button>

    <!-- Linha 2 -->
    <button class="win-btn btn-num" onclick="parent.postMessage('4', '*')">4</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('5', '*')">5</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('6', '*')">6</button>
    <button class="win-btn btn-op" onclick="parent.postMessage('-', '*')">-</button>

    <!-- Linha 3 -->
    <button class="win-btn btn-num" onclick="parent.postMessage('1', '*')">1</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('2', '*')">2</button>
    <button class="win-btn btn-num" onclick="parent.postMessage('3', '*')">3</button>
    <button class="win-btn btn-op" onclick="parent.postMessage('÷', '*')">÷</button>

    <!-- Linha 4 -->
    <button class="win-btn btn-num" onclick="parent.postMessage('0', '*')">0</button>
    <button class="win-btn btn-dot" onclick="parent.postMessage('.', '*')">.</button>
    <button class="win-btn btn-clear" onclick="parent.postMessage('C', '*')">C</button>
    <button class="win-btn btn-op" onclick="parent.postMessage('x', '*')">x</button>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- Capturar o clique dos botões HTML ---
# O Streamlit recebe os cliques via postMessage e executa a lógica Python
st.markdown("""
<script>
document.addEventListener('click', function(e) {
    if (e.target.tagName === 'BUTTON' && e.target.onclick) {
        // Simula clique para disparar o Streamlit
        e.target.click(); 
    }
});
</script>
""", unsafe_allow_html=True)
