import streamlit as st

# Page Configuration
st.set_page_config(page_title="Calculator", page_icon="🪶")

# --- STATE MANAGEMENT ---
if "expression" not in st.session_state:
    st.session_state.expression = ""

if "win_state" not in st.session_state:
    st.session_state.win_state = "normal"

# --- CALCULATOR FUNCTIONS ---
def add_to_calc(value):
    st.session_state.expression += str(value)

def clear_all():
    st.session_state.expression = ""

def clear_last():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate_result():
    try:
        expr = st.session_state.expression.replace("x", "*")
        result = str(eval(expr))
        st.session_state.expression = result
    except ZeroDivisionError:
        st.session_state.expression = "Error: Div/0"
    except Exception:
        st.session_state.expression = "Error"

def set_win_state(new_state):
    if st.session_state.win_state == new_state and new_state == "max":
        st.session_state.win_state = "normal"
    else:
        st.session_state.win_state = new_state

# --- CLOSED STATE ---
if st.session_state.win_state == "closed":
    st.warning("The calculator has been closed.")
    st.button("Open Calculator", on_click=set_win_state, args=("normal",))
    st.stop()

# --- ZOOM LOGIC ---
max_width = "700px" if st.session_state.win_state == "max" else "380px"

# --- CUSTOM CSS ---
st.markdown(f"""
    <style>
    .stApp {{
        background-color: #e5e5e5;
    }}
    
    /* CALCULATOR BODY */
    .block-container {{
        background-color: #ffffff;
        max-width: {max_width};
        padding: 15px 20px 20px 20px !important;
        margin-top: 5vh;
        border-radius: 12px;
        box-shadow: 
            0px 20px 30px rgba(0, 0, 0, 0.2), 
            0px 10px 10px rgba(0, 0, 0, 0.15),
            inset 0px -5px 15px rgba(0, 0, 0, 0.05);
        border: 1px solid #777;
        transition: max-width 0.3s ease-in-out;
    }}

    /* CALCULATOR DISPLAY */
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

    /* --- 3D CALCULATOR BUTTONS STYLE --- */
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

    /* --- TITLE BAR BUTTONS (CENTERED & SQUARED WITHOUT BORDERS) --- */
    div.stButton > button[title="Minimize"], 
    div.stButton > button[title="Maximize"], 
    div.stButton > button[title="Close"] {{
        background-color: transparent !important;
        color: #000 !important;
        box-shadow: none !important;
        border: none !important;
        outline: none !important;
        border-radius: 4px !important;
        height: 35px !important;
        width: 35px !important;
        font-size: 16px !important;
        padding: 0px !important;
        margin-top: -5px !important;
        margin-left: auto !important;
        margin-right: auto !important;
        transform: none !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }}
    
    /* FORÇAR CENTRALIZAÇÃO DOS ELEMENTOS INTERNOS DO STREAMLIT (DIV e P) */
    div.stButton > button[title="Minimize"] div, 
    div.stButton > button[title="Maximize"] div, 
    div.stButton > button[title="Close"] div,
    div.stButton > button[title="Minimize"] p, 
    div.stButton > button[title="Maximize"] p, 
    div.stButton > button[title="Close"] p {{
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        margin: 0 !important;
        padding: 0 !important;
        height: 100% !important;
        width: 100% !important;
        line-height: 1 !important;
    }}

    /* Efeitos de Hover (Passar o mouse) */
    div.stButton > button[title="Minimize"]:hover, 
    div.stButton > button[title="Maximize"]:hover {{
        background-color: #e5e5e5 !important;
        box-shadow: none !important;
        border: none !important;
        transform: none !important;
    }}
    
    div.stButton > button[title="Close"]:hover {{
        background-color: #e81123 !important;
        color: white !important;
        box-shadow: none !important;
        border: none !important;
        transform: none !important;
    }}

    /* Efeitos Active */
    div.stButton > button[title="Minimize"]:active, 
    div.stButton > button[title="Maximize"]:active, 
    div.stButton > button[title="Close"]:active {{
        transform: none !important;
        box-shadow: none !important;
    }}
    
    #MainMenu {{visibility: hidden;}}
    header {{visibility: hidden;}}
    </style>
""", unsafe_allow_html=True)

# --- TITLE BAR ---
col_icon, col_min, col_max, col_close = st.columns([7.2, 1, 1, 1])
with col_icon: 
    st.markdown("<div style='font-size: 14px; font-weight: 500; font-family: sans-serif; padding-top: 5px;'><span style='margin-right: 5px;'>🪶</span> Calculator</div>", unsafe_allow_html=True)
with col_min: 
    # Trocado para o traço simples para alinhar no centro sem problemas com a fonte
    st.button("-", key="btn_min", help="Minimize", on_click=set_win_state, args=("min",), use_container_width=True)
with col_max: 
    st.button("□", key="btn_max", help="Maximize", on_click=set_win_state, args=("max",), use_container_width=True)
with col_close: 
    st.button("✕", key="btn_close", help="Close", on_click=set_win_state, args=("closed",), use_container_width=True)

# --- CALCULATOR BODY ---
if st.session_state.win_state != "min":
    st.write("") 

    display_text = st.session_state.expression if st.session_state.expression != "" else "0"
    st.markdown(f'<div class="calc-display">{display_text}</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("CE", on_click=clear_last, use_container_width=True)
    with col2: st.button("C", on_click=clear_all, use_container_width=True)
    with col3: st.button("%", on_click=add_to_calc, args=("%",), use_container_width=True)
    with col4: st.button("/", on_click=add_to_calc, args=("/",), type="primary", use_container_width=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.button("7", on_click=add_to_calc, args=("7",), use_container_width=True)
    with col2: st.button("8", on_click=add_to_calc, args=("8",), use_container_width=True)
    with col3: st.button("9", on_click=add_to_calc, args=("9",), use_container_width=True)
    with col4: st.button("x", on_click=add_to_calc, args=("x",), type="primary", use_container_width=True)

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

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1: st.button("0", on_click=add_to_calc, args=("0",), use_container_width=True)
    with col2: st.button(".", on_click=add_to_calc, args=(".",), use_container_width=True)
    with col3: st.button("=", on_click=calculate_result, type="primary", use_container_width=True)
