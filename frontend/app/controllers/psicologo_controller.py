import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

def cadastrar_psicologo(psicologo_data):
    response = requests.post(f"{API_BASE_URL}/psicologos/", json=psicologo_data)
    if response.status_code == 200:
        st.success(f"Psicólogo {psicologo_data['nome']} cadastrado com sucesso!")
    else:
        st.error(f"Erro ao cadastrar psicólogo: {response.text}")
