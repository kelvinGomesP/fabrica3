import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

import streamlit as st
from pages.cadastro_paciente import cadastro_paciente  # Remova o .py
from pages.cadastro_psicologo import cadastro_psicologo  # Importa a função de cadastro de psicólogo

st.set_page_config(page_title="Cadastro de Pacientes", layout="wide")

# Menu de navegação
menu = ["Cadastro de Pacientes", "Cadastro de Psicólogo", "Outras Funcionalidades"]
choice = st.sidebar.selectbox("Selecione a Página", menu)

# Lógica de navegação
if choice == "Cadastro de Pacientes":
    cadastro_paciente()
elif choice == "Cadastro de Psicólogo":
    cadastro_psicologo()  # Chama a função de cadastro de psicólogo
elif choice == "Outras Funcionalidades":
    st.write("Funcionalidades futuras aqui...")
