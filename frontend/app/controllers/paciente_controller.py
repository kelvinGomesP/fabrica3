import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

def cadastrar_paciente(paciente_data):
    response = requests.post(f"{API_BASE_URL}/pacientes/", json=paciente_data)
    if response.status_code == 200:
        st.success(f"Paciente {paciente_data['nome']} cadastrado com sucesso!")
    else:
        st.error(f"Erro ao cadastrar paciente: {response.text}")

def listar_pacientes():
    response = requests.get(f"{API_BASE_URL}/pacientes/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao buscar pacientes")
        return []
