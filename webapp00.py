import streamlit as st

@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu Nome:")
senha = st.text_input("Digite sua Senha:", type="password")


if "vote" not in st.session_state:
    if st.button("Login"):
        if nome == 'admin' and senha == 'admin':
            st.session_state.logged_in = True
            st.success("Login bem-sucedido!")
        else:
            st.error("Nome de usuário ou senha incorretos.")
