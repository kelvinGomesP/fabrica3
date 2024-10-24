import requests
import streamlit as st

API_BASE_URL = "http://localhost:8000"

def cadastrar_medo(nome_medo: str, grau_medo: int):
    medo_data = {
        "nome_medo": nome_medo,
        "grau_medo": grau_medo
    }
    response = requests.post(f"{API_BASE_URL}/medos/", json=medo_data)
    if response.status_code == 200:
        st.success(f"Medo '{nome_medo}' cadastrado com sucesso!")
    else:
        st.error(f"Erro ao cadastrar medo: {response.text}")
