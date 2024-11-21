import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"  # Atualize se necessário

def criar_consulta(consulta_data):
    response = requests.post(f"{API_BASE_URL}/consultas/", json=consulta_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao criar consulta: {response.status_code} - {response.text}")

def listar_consultas():
    response = requests.get(f"{API_BASE_URL}/consultas/")
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Erro ao listar consultas: {response.status_code} - {response.text}")
