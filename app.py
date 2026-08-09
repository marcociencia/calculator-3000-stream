import streamlit as st

# Configuração inicial da página (layout='centered' para visualização compacta)
st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

# CSS Customizado
st.markdown("""
    <style>
    /* Fundo geral da página */
    .stApp {
        background-color: #ffffff;
    }

    /* Corpo principal da calculadora: levemente mais largo para o botão = */
    .block-container {
        max-width: 480px !important; 
        background-color: #f0f0f0; 
        padding: 2.5rem !important;
        border-radius: 8px;
        box-shadow: 0px 10px 30px rgba(0,0,0,0.2); 
        margin-top: 5vh;
    }

    /* Esconde cabeçalho e rodapé padrão do Streamlit */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Estilo do Visor ESTÁTICO (Fixo para não pular) */
    .visor {
        background-color: #ffffff;
        height: 80px !important; /* Altura fixa impede que o layout se mova */
        padding: 0 15px;
        border-top: 6px solid #a0a0a0;
        border-left: 6px solid #a0a0a0;
        border-bottom: 6px solid #ffffff;
        border-right: 6px solid #ffffff;
        margin-bottom: 20px;
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.1);
        
        /* Flexbox trava o texto no centro vertical e alinhado à direita */
        display: flex;
        align-items: center;
        justify-content: flex-end;
        overflow: hidden;
        box-sizing: border-box;
    }

    /* Força os parágrafos do Streamlit a não terem margem dentro do visor */
    .visor p, .visor span {
        margin: 0 !important;
        padding: 0 !important;
        font-size: 2rem !important;
        font-family: 'Verdana', sans-serif !important;
        color: black !important;
        line-height: 1 !important;
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
        padding: 0 !important;
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
        background-color: #800080 !important; 
        color: white !important; 
    }

    /* Coluna 4, Todos os botões (Operadores - Verde Claro até o x) */
    div[data-testid="column"]:nth-of-type(4) button {
        background-color: #90ee90 !important; 
        color: black !important; 
    }

    /* Coluna 5, 1º botão (Igual - Amarelo Esticado) */
    div[data-testid="column"]:nth-of-type(5) button {
        background-color: #ffd700 !important;
        height: 284px !important; 
    }
    </style>
""", unsafe_allow_html=True)

# Inicializando o state
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
# Troca o '*' por 'x' na hora de mostrar na tela. O &nbsp; garante que a div nunca fique vazia.
if st.session_state.expressao:
    texto_exibicao = st.session_state.expressao.replace('*', 'x')
else:
    texto_exibicao = "&nbsp;"
    
st.markdown(f'<div class="visor"><p>{texto_exibicao}</p></div>', unsafe_allow_html=True)

# Layout: 5 Colunas. A 5ª coluna tem peso '1.5', ficando mais larga.
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1.5], gap="small")

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
    # O botão mostra 'x', mas injeta '*' no código para o cálculo não dar erro
    st.button('x', on_click=press, args=('*',), use_container_width=True)

with col5:
    st.button('=', on_click=calcular, use_container_width=True)
