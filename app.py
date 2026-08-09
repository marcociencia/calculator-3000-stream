import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Calculadora", page_icon="🧮")

# CSS Customizado para recriar o visual 3D "Retrô" e as cores
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background-color: #f0f0f0;
    }

    /* Estilo do Visor idêntico à imagem */
    .visor {
        background-color: #ffffff;
        padding: 15px;
        /* Borda estilo Inset 3D profundo */
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
        background-color: #e0e0e0; /* Cinza claro padrão */
        color: black !important;
        border-top: 3px solid #ffffff !important;
        border-left: 3px solid #ffffff !important;
        border-bottom: 3px solid #666666 !important;
        border-right: 3px solid #666666 !important;
        border-radius: 0px !important; /* Cantos quadrados */
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

    /* Removendo o hover padrão do Streamlit para manter o design */
    div.stButton > button:hover, div.stButton > button:focus {
        box-shadow: none !important;
        border-color: transparent;
    }

    /* --- LÓGICA DE CORES ESPECÍFICAS VIA MARCADORES INVISÍVEIS --- */
    
    /* Botão Laranja (.) */
    div.element-container:has(.marker-orange) + div.element-container button {
        background-color: #ffa500 !important;
    }

    /* Botão Vermelho (C) */
    div.element-container:has(.marker-red) + div.element-container button {
        background-color: #ff0000 !important;
    }

    /* Botões Verdes (+, -, /, *) */
    div.element-container:has(.marker-green) + div.element-container button {
        background-color: #008000 !important;
    }

    /* Botão Amarelo (=) - Esticado para ocupar 4 linhas */
    div.element-container:has(.marker-yellow) + div.element-container button {
        background-color: #ffd700 !important;
        height: 284px !important; /* Altura calculada: 4 botões de 60px + 3 espaços */
    }
    </style>
""", unsafe_allow_html=True)

# Função auxiliar para injetar marcadores de cor antes dos botões específicos
def aplicar_cor(classe_cor):
    st.markdown(f'<div class="{classe_cor}" style="display:none;"></div>', unsafe_allow_html=True)

# Inicializando o state para guardar a expressão matemática
if 'expressao' not in st.session_state:
    st.session_state.expressao = ""

# Funções (Callbacks)
def press(num):
    # Se houve um erro anterior, limpa a tela antes de começar a digitar
    if st.session_state.expressao == " error ":
        st.session_state.expressao = ""
    st.session_state.expressao += str(num)

def limpar():
    st.session_state.expressao = ""

def calcular():
    try:
        # Avalia a expressão matemática armazenada
        resultado = str(eval(st.session_state.expressao))
        st.session_state.expressao = resultado
    except Exception:
        st.session_state.expressao = " error "

# Renderização do Visor
texto_visor = st.session_state.expressao if st.session_state.expressao else " "
st.markdown(f'<div class="visor">{texto_visor}</div>', unsafe_allow_html=True)

# Layout: 5 Colunas (Em vez de 4, para isolar o botão "=" na última)
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
    aplicar_cor('marker-orange')
    st.button('.', on_click=press, args=('.',), use_container_width=True)

with col3:
    st.button('9', on_click=press, args=('9',), use_container_width=True)
    st.button('6', on_click=press, args=('6',), use_container_width=True)
    st.button('3', on_click=press, args=('3',), use_container_width=True)
    aplicar_cor('marker-red')
    st.button('C', on_click=limpar, use_container_width=True) # type='primary' foi removido para não interferir

with col4:
    aplicar_cor('marker-green')
    st.button('+', on_click=press, args=('+',), use_container_width=True)
    aplicar_cor('marker-green')
    st.button('-', on_click=press, args=('-',), use_container_width=True)
    aplicar_cor('marker-green')
    st.button('/', on_click=press, args=('/',), use_container_width=True)
    aplicar_cor('marker-green')
    st.button('*', on_click=press, args=('*',), use_container_width=True)

with col5:
    aplicar_cor('marker-yellow')
    st.button('=', on_click=calcular, use_container_width=True)
