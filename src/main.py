import streamlit as st
from utils.utils import generate_text


# ---------- Page config ----------
st.theme = "dark"
st.title(":llama: Ollama Chat Bot")

col1, col2 = st.columns([1, 4])

# ---------- Session state ----------
if "messages" not in st.session_state:
    st.session_state.messages = []
    
prompt = st.chat_input("Type your message here...")

# ---------- LEFT COLUMN (controls) ----------
with col1:
    model = st.selectbox("Choose Ollama model", ["llama3.2", "llama3.2:1b", "phi4-mini", "gemma3:1b"])
    
    
    if st.button("New chat"):
        st.session_state.messages = []

# ---------- RIGHT COLUMN (chat) ----------
with col2: 
    # Display chat messages from history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]): 
            st.write(msg["content"])
    
    # User input
    with st.chat_message("user"):
        if prompt:
            st.write(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Bot response      
    with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                if prompt:
                    response = generate_text(model=model, prompt=f"Summarize the response if is over 1 paragraph without saying anything else: {prompt}")
                    st.write(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})

