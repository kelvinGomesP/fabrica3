import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import streamlit as st
from app.pages.cadastro_paciente import cadastro_paciente  # Remova o .py

st.set_page_config(page_title="Cadastro de Pacientes", layout="wide")

# Menu de navegação
menu = ["Cadastro de Pacientes", "Outras Funcionalidades"]
choice = st.sidebar.selectbox("Selecione a Página", menu)

if choice == "Cadastro de Pacientes":
    cadastro_paciente()
elif choice == "Outras Funcionalidades":
    st.write("Funcionalidades futuras aqui...")
