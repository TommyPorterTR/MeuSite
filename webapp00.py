import streamlit as st

st.set_page_config(layout="wide")
# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="data:image/png;base64,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" alt="Banner Image">
</div>
<style>
    .banner {
       width: 50%;
        height: 50px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""

# Display the custom HTML
st.components.v1.html(custom_html)

# Função para definir as cores de todos os elementos
def add_styles():
    st.markdown(
        """
        <style>
        /* Modificar a cor de todos os textos (cor dourada para o conteúdo geral) */
        .css-1d391kg, .css-1v0mbdj, .css-1b6t85b, .css-1v4t7gx {
            color: #DAA520 !important;  /* Cor dourada para todos os textos */
        }

        /* Modificar a cor das perguntas (labels) para amarelo */
        label {
            color: #FFFF00 !important;  /* Cor amarela para as perguntas */
        }

        /* Alterar a cor de fundo do botão */
        .css-1v4t7gx {
            background-color: #DAA520 !important;  /* Cor dourada para o botão */
            color: white !important;  /* Cor do texto do botão */
        }

        /* Modificar a cor dos campos de texto */
        .stTextInput input, .stTextArea textarea {
            color: #FFFAF0 !important;  /* Cor dourada para os campos de texto */
        }
        </style>
        """, unsafe_allow_html=True)

# Função de login
def login_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    senha = st.text_input("Digite sua senha:", type="password")

    # Verifica se o botão de login foi clicado
    if st.button("Login"):
        if nome == 'admin' and senha == 'admin':  # Simples verificação de login
            st.session_state.logged_in = True  # Marca como logado
            st.session_state.page = "form"  # Redireciona para o formulário após login
            st.success("Login bem-sucedido!")
        else:
            st.error("Nome de usuário ou senha incorretos.")

# Função para o formulário
def form_page():
    ID = st.text_input("Digite seu ID:")
    nome = st.text_input("Digite seu nome:")
    email = st.text_input("Digite seu e-mail:")
    prioridade = st.selectbox("Prioridade: ", ("Baixa", "Média", "Alta", "*Crítico*"))
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
    url = base_url + "&".join([f"{k}={v}" for k, v in params.items()])

    # Botão de envio para o Google Forms
    if st.button("Enviar"):
        st.write("Formulário enviado com sucesso!")
        # Redirecionar para o Google Forms com os dados preenchidos
        st.markdown(f'<a href="{url}" target="_blank">Clique aqui para enviar seus dados</a>', unsafe_allow_html=True)

# Adiciona as alterações de estilo
add_styles()

# Verifica se o usuário está logado e decide qual página exibir
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()  # Exibe a página de login se o usuário não estiver logado
else:
    form_page()  # Exibe o formulário se o usuário estiver logado
