import streamlit as st
import urllib.parse

# Definindo a configuração da página para layout "wide"
st.set_page_config(layout="wide")

# Mandando ler arquivo CSS
with open("style.css") as f:
  st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Adicionando HTML estilizado para cabeçalho
st.html(
  "<div><div style='background-color:white; margin=0; padding: 20px; height: 150px; text-align:center;'><div><img src='https://brasil.campus-party.org/wp-content/uploads/2023/08/Logo_Tectoy.png' style='max-height:120px; padding: 10px;'></div></div><div style='background-color: yellow; text-align:center;height:70px;'><h2 style='font-size: 28px; font-weight: bold; color:black;'>Abertura de Chamado</h2></div></div>"
)

# Função de login
def login_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")

    if st.button("Login"):
        if nome == 'admin' and senha == 'admin':  # Simples verificação de login
            st.session_state.logged_in = True
            st.session_state.page = "form"  # Redireciona para o formulário após login
            st.success("Login bem-sucedido!")
        else:
            st.error("Nome de usuário ou senha incorretos.")

# Função para o formulário
def form_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    email = st.text_input("Digite seu e-mail:")
    prioridade = st.selectbox("Prioridade: ", ("Baixa", "Média", "Alta", "Crítico"))
    assunto = st.text_input("Assunto: ")
    mensagem = st.text_input("Mensagem: ")

    # Criando o link para o Google Forms com os dados
    base_url = "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?"
    params = {
        "entry.69514635": ID,
        "entry.1100048191": nome,
        "entry.8340763": email,
        "entry.398253139": prioridade,
        "entry.618138322": assunto,
        "entry.1550799906": mensagem
    }

    # Codificando os parâmetros para a URL
    url = base_url + urllib.parse.urlencode(params)

    # Botão de envio para o Google Forms
    if st.button("Enviar"):
        st.write("Formulário enviado com sucesso!")
        # Redirecionar para o Google Forms com os dados preenchidos
        st.markdown(f'<a href="{url}" target="_blank">Clique aqui para enviar seus dados</a>', unsafe_allow_html=True)

# Verifica se o usuário está logado e decide qual página exibir
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()  # Exibe a página de login se o usuário não estiver logado
else:
    form_page()  # Exibe o formulário se o usuário estiver logado
