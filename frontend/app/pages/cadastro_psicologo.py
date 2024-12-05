import streamlit as st
from controllers.psicologo_controller import cadastrar_psicologo  # Importa a função para cadastrar o psicólogo
from func.back_to_home import render_back_to_home_button

def cadastro_psicologo():
    render_back_to_home_button()
    st.title("Cadastro de Psicólogo")

    st.markdown("Preencha as informações abaixo para cadastrar um novo psicólogo.")
    
    with st.form("cadastro_psicologo_form"):
        # Organização com colunas
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome do Psicólogo", placeholder="Ex: João Silva")
            email = st.text_input("E-mail", placeholder="Ex: joao.silva@email.com")
            especialidade = st.text_input("Especialidade", placeholder="Ex: Terapia Cognitiva")
        
        with col2:
            cpf = st.text_input("CPF (apenas números)", max_chars=11, placeholder="Ex: 12345678901")
            telefone = st.text_input("Telefone (DDD + número)", max_chars=11, placeholder="Ex: 11999999999")
            crp = st.text_input("CRP (Registro Profissional)", max_chars=10, placeholder="Ex: 12345/XX")
        
        submit_button = st.form_submit_button("Cadastrar Psicólogo")

        # Validações em tempo real
        if submit_button:
            if not nome:
                st.error("O campo 'Nome' é obrigatório.")
            elif len(cpf) != 11 or not cpf.isdigit():
                st.error("CPF inválido. Deve conter exatamente 11 dígitos numéricos.")
            elif len(telefone) != 11 or not telefone.isdigit():
                st.error("Telefone inválido. Deve conter DDD + 9 dígitos (ex: 11999999999).")
            elif not email or "@" not in email:
                st.error("E-mail inválido. Insira um endereço de e-mail válido.")
            elif not crp:
                st.error("O campo 'CRP' é obrigatório.")
            else:
                # Cadastro bem-sucedido
                psicologo_data = {
                    "nome": nome,
                    "cpf": cpf,
                    "telefone": telefone,
                    "email": email,
                    "especialidade": especialidade,
                    "crp": crp
                }
                cadastrar_psicologo(psicologo_data)
                st.success(f"Psicólogo {nome} cadastrado com sucesso!")

# Executar a página
if __name__ == "__main__":
    cadastro_psicologo()
