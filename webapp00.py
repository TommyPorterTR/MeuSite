import streamlit as st

# Função para adicionar a imagem de fundo e definir a cor da fonte
def add_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .reportview-container {{
            background: url("{image_url}");
            background-size: cover;  /* Garante que a imagem cubra toda a tela */
            background-position: center;  /* Centraliza a imagem */
            background-attachment: fixed; /* Garante que a imagem não se mova quando rolar a página */
            height: 100vh; /* 100% da altura da tela */
            width: 100%;
            position: absolute;
            top: 0;
            left: 0;
            z-index: -1; /* Garante que o conteúdo ficará acima da imagem */
        }}

        /* Modificar a cor da fonte de todos os textos */
        .css-1d391kg {
            color: #FFFFFF;  /* Cor branca para o texto */
        }

        /* Modificar a cor do texto dos títulos */
        .css-1v0mbdj {
            color: #ff6347;  /* Cor vermelha para títulos */
        }

        /* Modificar a cor do texto dos inputs e outros campos de texto */
        .css-1b6t85b {
            color: #FFFF00;  /* Cor amarela para campos de texto */
        }

        /* Alterar a cor do botão */
        .css-1v4t7gx {
            background-color: #4CAF50;  /* Cor verde para o botão */
            color: white;  /* Cor do texto do botão */
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

# Adiciona a imagem de fundo (coloque a URL da imagem desejada entre aspas)
image_url = "https://assets.folhavitoria.com.br/images/a0322d70-1f5c-11ef-9ec9-9f1d3c6a39fe--minified.jpg"  # Substitua com a URL correta da imagem
add_background_image(image_url)

# Verifica se o usuário está logado e decide qual página exibir
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()  # Exibe a página de login se o usuário não estiver logado
else:
    form_page()  # Exibe o formulário se o usuário estiver logado
