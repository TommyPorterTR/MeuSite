import streamlit as st

# Função para definir as cores de todos os elementos
def add_styles():
    st.markdown(
        """
        <style>
        /* Modificar a cor de todos os textos */
        .css-1d391kg, .css-1v0mbdj, .css-1b6t85b, .css-1v4t7gx {
            color: #DAA520 !important;  /* Cor dourada para todos os textos */
        }

        /* Alterar a cor de fundo do botão */
        .css-1v4t7gx {
            background-color: #DAA520 !important;  /* Cor dourada para o botão */
            color: white !important;  /* Cor do texto do botão */
        }

        /* Modificar a cor dos campos de texto */
        .stTextInput input, .stTextArea textarea {
            color: #FFFFFF !important;  /* Cor dourada para os campos de texto */
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
