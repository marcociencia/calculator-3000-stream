import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# CSS Customizado para replicar o design exato e fixar o visor estático
st.markdown("""
    <style>
    /* Fundo geral da página */
    .stApp {
        background-color: #ffffff;
    }

    /* Caixa principal da calculadora (centralizada e com fundo cinza claro) */
    .block-container {
        max-width: 450px !important; 
        background-color: #f0f0f0; 
        padding: 2.5rem !important;
        border-radius: 8px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2); 
        margin-top: 5vh;
    }

    /* Esconde cabeçalho e rodapé padrão do Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Visor ESTÁTICO (altura fixa e flexbox impedem que ele pule ao digitar) */
    .visor {
        background-color: #ffffff;
        height: 80px !important;
        padding: 0 15px;
        border-top: 6px solid #a0a0a0;
        border-left: 6px solid #a0a0a0;
        border-bottom: 6px solid #ffffff;
        border-right: 6px solid #ffffff;
        margin-bottom: 20px;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1);
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
        box-sizing: border-box;
    }

    .visor p {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 2rem !important;
        font-family: 'Verdana', sans-serif !important;
        color: black !important;
        line-height: 1 !important;
    }

    /* Estilo base dos botões (Efeito 3D Outset) */
    div.stButton > button {
        background-color: gainsboro;
        color: black !important;
        border-top: 3px solid #ffffff !important;
        border-left: 3px solid #ffffff !important;
        border-bottom: 3px solid #666666 !important;
        border-right: 3px solid #666666 !important;
        border-radius: 0px !important;
        font-weight: bold;
        font-size: 1.2rem;
        height: 60px;
        width: 100%;
        transition: none; 
        padding: 0 !important;
    }
    
    div.stButton > button:active {
        border-top: 3px solid #666666 !important;
        border-left: 3px solid #666666 !important;
        border-bottom: 3px solid #ffffff !important;
        border-right: 3px solid #ffffff !important;
    }

    div.stButton > button:hover, div.stButton > button:focus {
        box-shadow: none !important;
    }

    /* --- CORES ESPECÍFICAS DOS BOTÕES --- */

    /* Botão Ponto (.) - Laranja */
    div[data-testid="column"]:nth-of-type(2) div.element-container:nth-child(4) button {
        background-color: orange !important;
    }

    /* Botão C - Roxo */
    div[data-testid="column"]:nth-of-type(3) div.element-container:nth-child(4) button {
        background-color: #800080 !important; 
        color: white !important; 
    }

    /* Operadores (+, -, /, x) - Verde Claro */
    div[data-testid="column"]:nth-of-type(4) button {
        background-color: #90ee90 !important; 
        color: black !important; 
    }

    /* Coluna 5: Botão Igual (=) esticado verticalmente e amarelo */
    div[data-testid="column"]:nth-of-type(5),
    div[data-testid="column"]:nth-of-type(5) > div,
    div[data-testid="column"]:nth-of-type(5) > div > div {
        height: 100% !important;
        display: flex !important;
        flex-direction: column !important;
    }

    div[data-testid="column"]:nth-of-type(5) button {
        background-color: #FFD700 !important;
        flex-grow: 1 !important;
        height: auto !important;
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# Gerenciamento do estado da expressão (equivalente ao StringVar do seu código)
if 'expressao' not in st.session_state:
    st.session_state.expressao = ""

def press(num):
    if st.session_state.expressao == " error ":
        st.session_state.expressao = ""
    st.session_state.expressao += str(num)

def limpar():
    st.session_state.expressao = ""

def teclaigual():
    try:
        total = str(eval(st.session_state.expressao))
        st.session_state.expressao = total
    except Exception:
        st.session_state.expressao = " error "

# Renderização do Visor Estático (substitui '*' por 'x' visualmente)
texto_exibicao = st.session_state.expressao.replace('*', 'x') if st.session_state.expressao else "&nbsp;"
st.markdown(f'<div class="visor"><p>{texto_exibicao}</p></div>', unsafe_allow_html=True)

# Layout em 5 colunas correspondente à sua estrutura original
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.2], gap="small")

with col1:
    st.button('7', on_click=press, args=('7',), use_container_width=True)
    st.button('4', on_click=press, args=('4',), use_container_width=True)
    st.button('1', on_click=press, args=('1',), use_container_width=True)
    st.button('0', on_click=press, args=('0',), use_container_width=True)

with col2:
    st.button('8', on_click=press, args=('8',), use_container_width=True)
    st.button('5', on_click=press, args=('5',), use_container_width=True)
    st.button('2', on_click=press, args=('2',), use_container_width=True)
    st.button('.', on_click=press, args=('.',), use_container_width=True)

with col3:
    st.button('9', on_click=press, args=('9',), use_container_width=True)
    st.button('6', on_click=press, args=('6',), use_container_width=True)
    st.button('3', on_click=press, args=('3',), use_container_width=True)
    st.button('C', on_click=limpar, use_container_width=True)

with col4:
    st.button('+', on_click=press, args=('+',), use_container_width=True)
    st.button('-', on_click=press, args=('-',), use_container_width=True)
    st.button('/', on_click=press, args=('/',), use_container_width=True)
    # Mostra 'x' na tela, mas computa '*' internamente
    st.button('x', on_click=press, args=('*',), use_container_width=True)

with col5:
    st.button('=', on_click=teclaigual, use_container_width=True)
