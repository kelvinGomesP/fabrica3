import sys
import os
import streamlit as st



from pages.cadastro_paciente import cadastro_paciente  # Remova o .py
from pages.cadastro_psicologo import cadastro_psicologo
from pages.tempo_real import *
from pages.consultas_page import consultas_page  # Importa a página de consultas

st.set_page_config(page_title="Gestão Clínica", layout="wide")

# Menu de navegação
menu = [
    "Cadastro de Pacientes",
    "Cadastro de Psicólogo",
    "Cadastro de Consultas",  # Novo menu para consultas
    "Tempo Real",
    "Outras Funcionalidades"
]
choice = st.sidebar.selectbox("Selecione a Página", menu)

# Lógica de navegação
if choice == "Cadastro de Pacientes":
    cadastro_paciente()
elif choice == "Cadastro de Psicólogo":
    cadastro_psicologo()
elif choice == "Cadastro de Consultas":
    consultas_page()  # Chama a página de consultas
elif choice == "Tempo Real":
    visualizar_paciente()
elif choice == "Outras Funcionalidades":
    st.write("Funcionalidades futuras aqui...")
