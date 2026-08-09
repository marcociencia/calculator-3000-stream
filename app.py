import streamlit as st

# --- Page Configuration ---
st.set_page_config(
    page_title="Stylish Calculator",
    page_icon="🧮",
    layout="centered"
)

# --- Custom CSS for "Stylish" Look ---
st.markdown("""
<style>
    .stTextInput > div > div > input {
        font-size: 40px;
        font-weight: bold;
        font-family: 'Courier New', monospace;
        text-align: right;
        padding: 15px;
        border: 2px solid #333;
        border-radius: 10px;
    }
    .calc-btn {
        font-size: 24px;
        height: 60px;
        width: 100%;
        margin-bottom: 10px;
        border-radius: 8px;
        background-color: #f0f2f6;
        border: 1px solid #ddd;
    }
    .calc-btn:hover {
        background-color: #e0e2e6;
        border-color: #555;
    }
    .math-line {
        font-family: monospace;
        font-size: 20px;
        color: #444;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- Session State Management ---
if 'first_num' not in st.session_state:
    st.session_state.first_num = ""
if 'operator' not in st.session_state:
    st.session_state.operator = ""
if 'second_num' not in st.session_state:
    st.session_state.second_num = ""
if 'result' not in st.session_state:
    st.session_state.result = ""
if 'display_state' not in st.session_state:
    st.session_state.display_state = "input_primary"  # States: input_primary, op_chosen, input_secondary

# --- Helper Functions ---
def update_display():
    """Constructs the visual text based on the current state."""
    display_text = ""
    
    if st.session_state.display_state == "input_primary":
        display_text = st.session_state.first_num
    elif st.session_state.display_state == "op_chosen" or st.session_state.display_state == "input_secondary":
        # Draw the first line
        line1 = f"{st.session_state.first_num}"
        # Add the operator properly spaced (like the image provided)
        op_display = f"  {st.session_state.operator}  "
        # Draw the second line (operator + secondary num)
        line2 = f"{op_display}{st.session_state.second_num}"
        # Draw the line
        divider = "─" * 15 
        # Draw the result
        line3 = f"{st.session_state.result}"
        
        display_text = f"{line1}\n{line2}\n{divider}\n{line3}"
    
    return display_text

def button_clicked(value):
    """Handles button clicks logic."""
    current_state = st.session_state.display_state
    
    if current_state == "input_primary":
        if value in "0123456789":
            st.session_state.first_num += value
    
    elif current_state == "input_secondary":
        if value in "0123456789":
            st.session_state.second_num += value
        # If user enters a 2-digit number, allow it (0-10 logic implied by pressing 0, then 0 for 10)
    
    # Operator Logic
    if value in "+-x":
        # If pressing operator after secondary number, calculate first
        if st.session_state.second_num != "":
            calculate_result()
            st.session_state.first_num = st.session_state.result
            st.session_state.second_num = ""
        
        st.session_state.operator = value
        st.session_state.display_state = "op_chosen" # Break line and move down

    # Equals Logic
    if value == "=":
        calculate_result()
        st.session_state.display_state = "input_primary" # Reset for next calculation
        st.session_state.first_num = st.session_state.result
        st.session_state.second_num = ""
        st.session_state.operator = ""

    # Clear
    if value == "C":
        st.session_state.first_num = ""
        st.session_state.second_num = ""
        st.session_state.operator = ""
        st.session_state.result = ""
        st.session_state.display_state = "input_primary"

def calculate_result():
    """Performs math operation."""
    if st.session_state.first_num and st.session_state.second_num:
        n1 = int(st.session_state.first_num)
        n2 = int(st.session_state.second_num)
        op = st.session_state.operator
        
        if op == "+":
            st.session_state.result = str(n1 + n2)
        elif op == "-":
            st.session_state.result = str(n1 - n2)
        elif op == "x":
            st.session_state.result = str(n1 * n2)
    else:
        st.session_state.result = "Err"

# --- UI Layout ---
st.title("🧮 Style Calculator 3000")

# Display Area
display_content = update_display()
st.text_area("Calculator Display", value=display_content, height=200, key="display", label_visibility="collapsed")

# Row 1: Numbers 0-9
cols = st.columns(5)
for i, num in enumerate(["1", "2", "3", "4", "5"]):
    with cols[i]:
        if st.button(num, key=f"btn_{num}"):
            button_clicked(num)

cols = st.columns(5)
for i, num in enumerate(["6", "7", "8", "9", "0"]):
    with cols[i]:
        if st.button(num, key=f"btn_{num}"):
            button_clicked(num)

# Row 2: Operations and Actions
cols = st.columns(5)
operators = ["+", "-", "x", "=", "C"]
for i, op in enumerate(operators):
    with cols[i]:
        if st.button(op, key=f"btn_{op}"):
            button_clicked(op)

st.markdown("---")
st.caption("Build logic: Primary > Operator (Break & Line) > Secondary > Result")