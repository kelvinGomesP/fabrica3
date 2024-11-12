import streamlit as st
from controllers.psicologo_controller import cadastrar_psicologo  # Importa a função para cadastrar o psicólogo

def cadastro_psicologo():
    st.title("Cadastro de Psicólogo")

    with st.form("cadastro_psicologo_form"):
        nome = st.text_input("Nome do Psicólogo")
        
        cpf = st.text_input("CPF (apenas números)", max_chars=11)
        if cpf and not (cpf.isdigit() and len(cpf) == 11):
            st.error("O CPF deve ter exatamente 11 dígitos numéricos.")
        
        telefone = st.text_input("Telefone (formato: DDD + número)", max_chars=11)
        if telefone and not (telefone.isdigit() and len(telefone) == 11):
            st.error("O Telefone deve ter o formato DDD + 9 dígitos (ex: 11999999999).")

        email = st.text_input("E-mail")
        especialidade = st.text_input("Especialidade")
        crp = st.text_input("CRP (Registro Profissional)", max_chars=10)  # Novo campo para o CRP

        submit_button = st.form_submit_button("Cadastrar Psicólogo")

    if submit_button:
        # Validação dos campos CPF e Telefone
        if len(cpf) == 11 and cpf.isdigit() and len(telefone) == 11 and telefone.isdigit():
            psicologo_data = {
                "nome": nome,
                "cpf": cpf,
                "telefone": telefone,
                "email": email,
                "especialidade": especialidade,
                "crp": crp  # Agora inclui o campo CRP
            }
            cadastrar_psicologo(psicologo_data)
        else:
            st.error("Certifique-se de que CPF e Telefone estão no formato correto.")
