import streamlit as st

# Configuração inicial da página
st.set_page_config(page_title="Calculadora", page_icon="🧮")

# CSS Customizado para criar o "visor" da calculadora
st.markdown("""
    <style>
    .visor {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 5px;
        border: 2px inset #ccc;
        text-align: right;
        font-size: 2rem;
        font-family: 'Verdana', sans-serif;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("Calculadora")

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
texto_visor = st.session_state.expressao if st.session_state.expressao else "0"
st.markdown(f'<div class="visor">{texto_visor}</div>', unsafe_allow_html=True)

# Layout: Grade de Botões
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(' 7 ', on_click=press, args=('7',), use_container_width=True)
    st.button(' 4 ', on_click=press, args=('4',), use_container_width=True)
    st.button(' 1 ', on_click=press, args=('1',), use_container_width=True)
    st.button(' 0 ', on_click=press, args=('0',), use_container_width=True)

with col2:
    st.button(' 8 ', on_click=press, args=('8',), use_container_width=True)
    st.button(' 5 ', on_click=press, args=('5',), use_container_width=True)
    st.button(' 2 ', on_click=press, args=('2',), use_container_width=True)
    st.button(' . ', on_click=press, args=('.',), use_container_width=True)

with col3:
    st.button(' 9 ', on_click=press, args=('9',), use_container_width=True)
    st.button(' 6 ', on_click=press, args=('6',), use_container_width=True)
    st.button(' 3 ', on_click=press, args=('3',), use_container_width=True)
    st.button(' C ', on_click=limpar, type='primary', use_container_width=True)

with col4:
    st.button(' + ', on_click=press, args=('+',), use_container_width=True)
    st.button(' - ', on_click=press, args=('-',), use_container_width=True)
    st.button(' / ', on_click=press, args=('/',), use_container_width=True)
    st.button(' * ', on_click=press, args=('*',), use_container_width=True)

# O botão de "=" fica abaixo ocupando as 4 colunas em largura
st.button(' = ', on_click=calcular, type='primary', use_container_width=True)
