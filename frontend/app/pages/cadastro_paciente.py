import streamlit as st
from datetime import date
from controllers.paciente_controller import cadastrar_paciente
from controllers.medo_controller import cadastrar_medo

def cadastro_paciente():
    st.title("Cadastro de Paciente")

    with st.form("cadastro_paciente_form"):
        nome = st.text_input("Nome")
        
        # Data de Nascimento com limite mínimo de 1920 e sem limite máximo
        data_nascimento = st.date_input(
            "Data de Nascimento", 
            value=date(2000, 1, 1), 
            min_value=date(1920, 1, 1)
        )
        
        # Limitar CPF a 11 dígitos
        cpf = st.text_input("CPF (apenas números)", max_chars=11)
        
        # Formatação e limite para o telefone (DD) XXXXX-XXXX
        telefone = st.text_input("Telefone (formato: (XX) XXXXX-XXXX)")
        
        email = st.text_input("E-mail")
        endereco = st.text_area("Endereço")
        observacao = st.text_area("Observações")
        
        # Relacionado ao medo
        st.subheader("Medo Relacionado")
        nome_medo = st.text_input("Nome do Medo")
        grau_medo = st.slider("Grau do Medo", 0, 10)

        submit_button = st.form_submit_button("Cadastrar")

    if submit_button:
        # Validar telefone para (XX) XXXXX-XXXX
        if not telefone.isdigit() or len(telefone) != 11:
            st.error("Telefone deve ter 11 dígitos no formato correto!")
        else:
            paciente_data = {
                "nome": nome,
                "data_nascimento": str(data_nascimento),
                "cpf": cpf,
                "telefone": telefone,
                "email": email,
                "endereco": endereco,
                "observacao": observacao
            }
            cadastrar_paciente(paciente_data)
            cadastrar_medo(nome_medo, grau_medo)
            st.success("Paciente e medo cadastrados com sucesso!")
