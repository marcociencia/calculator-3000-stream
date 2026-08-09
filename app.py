import streamlit as st

# Configuração inicial da página (layout='centered' para visualização compacta)
st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# CSS Customizado
st.markdown("""
    <style>
    /* Fundo geral da página (fora da calculadora) */
    .stApp {
        background-color: #ffffff;
    }

    /* Corpo principal da calculadora: limita o tamanho, adiciona o fundo cinza retro da imagem e uma sombra */
    .block-container {
        max-width: 450px !important; 
        background-color: #f0f0f0; /* Cinza claro idêntico à carcaça na imagem */
        padding: 2.5rem !important;
        border-radius: 8px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2); 
        margin-top: 5vh;
    }

    /* Esconde cabeçalho e rodapé padrão do Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Estilo do Visor idêntico à imagem (Inset 3D) */
    .visor {
        background-color: #ffffff;
        padding: 15px;
        border-top: 6px solid #a0a0a0;
        border-left: 6px solid #a0a0a0;
        border-bottom: 6px solid #ffffff;
        border-right: 6px solid #ffffff;
        text-align: right;
        font-size: 2rem;
        font-family: 'Verdana', sans-serif;
        margin-bottom: 20px;
        color: black;
        min-height: 75px;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1);
    }

    /* Estilo base (Outset 3D) para TODOS os botões */
    div.stButton > button {
        background-color: #e0e0e0;
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
    }
    
    /* Efeito de clique (afundando o botão) */
    div.stButton > button:active {
        border-top: 3px solid #666666 !important;
        border-left: 3px solid #666666 !important;
        border-bottom: 3px solid #ffffff !important;
        border-right: 3px solid #ffffff !important;
    }

    /* Removendo o hover padrão do Streamlit */
    div.stButton > button:hover, div.stButton > button:focus {
        box-shadow: none !important;
    }

    /* --- CORES ESPECÍFICAS --- */

    /* Coluna 2, 4º botão (Ponto - Laranja) */
    div[data-testid="column"]:nth-of-type(2) div.element-container:nth-child(4) button {
        background-color: #ffa500 !important;
    }

    /* Coluna 3, 4º botão (C - Roxo) */
    div[data-testid="column"]:nth-of-type(3) div.element-container:nth-child(4) button {
        background-color: #800080 !important; /* Roxo clássico */
        color: white !important; 
    }

    /* Coluna 4, Todos os botões (Operadores - Verde Claro) */
    div[data-testid="column"]:nth-of-type(4) button {
        background-color: #90ee90 !important; /* Verde claro (LightGreen) */
        color: black !important; /* Texto preto para dar contraste com o verde claro */
    }

    /* Coluna 5, 1º botão (Igual - Amarelo Esticado) */
    div[data-testid="column"]:nth-of-type(5) button {
        background-color: #ffd700 !important;
        height: 284px !important; /* Altura exata para alinhar com os 4 botões ao lado */
    }
    </style>
""", unsafe_allow_html=True)

# Inicializando o state para guardar a expressão matemática
if 'expressao' not in st.session_state:
    st.session_state.expressao = ""

# Funções (Callbacks)
def press(num):
    if st.session_state.expressao == " error ":
        st.session_state.expressao = ""
    st.session_state.expressao += str(num)

def limpar():
    st.session_state.expressao = ""

def calcular():
    try:
        resultado = str(eval(st.session_state.expressao))
        st.session_state.expressao = resultado
    except Exception:
        st.session_state.expressao = " error "

# Renderização do Visor
texto_visor = st.session_state.expressao if st.session_state.expressao else " "
st.markdown(f'<div class="visor">{texto_visor}</div>', unsafe_allow_html=True)

# Layout limpo: 5 Colunas 
col1, col2, col3, col4, col5 = st.columns(5, gap="small")

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
    st.button('*', on_click=press, args=('*',), use_container_width=True)

with col5:
    st.button('=', on_click=calcular, use_container_width=True)
