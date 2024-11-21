import streamlit as st
import pandas as pd
import urllib3
from urllib3 import request
from io import BytesIO
import request

form = st.form("formHD")
ID = st.text_input("Digite seu ID:")
nome = st.text_input("Digite seu nome:")
email = st.text_input("Digite seu e-mail:")
prioridade = st.selectbox("Prioridade: ",("Baixa", "Medio", "Alta", "Critico"))
assunto = st.text_input("Assunto: ")
mensagem = st.text_input("Messagem: ")
arquivos = st.file_uploader('Uploader de Arquivo')

botao = st.link_button("Enviar", "https://docs.google.com/forms/d/e/1FAIpQLSe0_2DQ533BSUEuWf9haVK7w6oUkMei_kFphG-MKGwvA9_bzQ/formResponse?&submit=Enviar?usp=pp_url&entry")

rd = request.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vQNW3ECuL6022Cg-ZUAiC4eHpW6INB2PLhtm_8jiWHTkdNdkhYEB71XptIbooT_pLmjURLz5ihSLBkH/pub?gid=812473058&single=true&output=csv')
