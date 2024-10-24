import streamlit as st
from app.controllers.paciente_controller import listar_pacientes

def listar_pacientes_page():
    st.title("Lista de Pacientes")
    
    pacientes = listar_pacientes()
    
    if pacientes:
        for paciente in pacientes:
            st.subheader(f"Paciente: {paciente['nome']}")
            st.write(f"CPF: {paciente['cpf']}")
            st.write(f"Telefone: {paciente['telefone']}")
            st.write(f"E-mail: {paciente['email']}")
            st.write(f"Endereço: {paciente['endereco']}")
            st.write(f"Observação: {paciente['observacao']}")
            st.write("---")
