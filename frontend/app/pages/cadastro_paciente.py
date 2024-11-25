import streamlit as st
from datetime import date
from controllers.paciente_controller import cadastrar_paciente
from controllers.medo_controller import cadastrar_medo


def cadastro_paciente():
    st.title("Cadastro de Paciente")

    with st.form("cadastro_paciente_form"):
        nome = st.text_input("Nome")
        data_nascimento = st.date_input("Data de Nascimento", value=date(2000, 1, 1), min_value=date(1920, 1, 1))
        cpf = st.text_input("CPF (apenas números)", max_chars=11)
        telefone = st.text_input("Telefone (apenas números)", max_chars=11)
        email = st.text_input("E-mail")
        endereco = st.text_area("Endereço")
        observacao = st.text_area("Observações")

        # Dados de Medo
        st.subheader("Medo Relacionado")
        nome_medo = st.text_input("Nome do Medo")
        grau_medo = st.slider("Grau do Medo", 0, 10)

        submit_button = st.form_submit_button("Cadastrar")

    if submit_button:
        if not telefone.isdigit() or len(telefone) != 11:
            st.error("Telefone deve ter 11 dígitos!")
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

# Executar a página
if __name__ == "__main__":
    cadastro_paciente()

