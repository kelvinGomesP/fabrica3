import streamlit as st
from datetime import date
from controllers.paciente_controller import cadastrar_paciente
from func.back_to_home import render_back_to_home_button

def validar_cpf(cpf):
    return cpf.isdigit() and len(cpf) == 11

def validar_telefone(telefone):
    return telefone.isdigit() and len(telefone) == 11

def validar_email(email):
    return "@" in email and "." in email

def cadastro_paciente():
    render_back_to_home_button()
    st.title("Cadastro de Paciente")

    with st.form("cadastro_paciente_form"):
        st.subheader("Dados do Paciente")
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome")
            data_nascimento = st.date_input("Data de Nascimento", value=date(2000, 1, 1), min_value=date(1920, 1, 1))
        with col2:
            cpf = st.text_input("CPF (somente números)", max_chars=11, help="Digite os 11 dígitos do CPF")
            telefone = st.text_input("Telefone (somente números)", max_chars=11, help="Ex.: 11987654321")

        email = st.text_input("E-mail", help="Digite um e-mail válido")
        endereco = st.text_area("Endereço")
        observacao = st.text_area("Observações")

        # Dados de Medo
        st.subheader("Medo Relacionado")
        nome_medo = st.text_input("Nome do Medo")
        grau_medo = st.slider("Grau do Medo", 0, 10, help="Avalie o grau do medo em uma escala de 0 a 10")

        submit_button = st.form_submit_button("Cadastrar")

    if submit_button:
        erros = []
        if not validar_cpf(cpf):
            erros.append("CPF deve conter 11 dígitos numéricos.")
        if not validar_telefone(telefone):
            erros.append("Telefone deve conter 11 dígitos numéricos.")
        if not validar_email(email):
            erros.append("E-mail inválido.")

        if erros:
            for erro in erros:
                st.error(erro)
        else:
            paciente_data = {
                "nome": nome,
                "data_nascimento": str(data_nascimento),
                "cpf": cpf,
                "telefone": telefone,
                "email": email,
                "endereco": endereco,
                "observacao": observacao,
                "medo": {
                    "nome_medo": nome_medo,
                    "grau_medo": grau_medo
                }
            }
            cadastrar_paciente(paciente_data)
            st.success("Paciente cadastrado com sucesso!")
            st.balloons()

# Executar a página
if __name__ == "__main__":
    cadastro_paciente()
