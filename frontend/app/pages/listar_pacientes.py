import streamlit as st
from controllers.paciente_controller import listar_pacientes

def listar_pacientes_page():
    # Título da página
    st.title("Lista de Pacientes")

    # Filtro de busca por nome
    filtro_nome = st.text_input("Buscar por Nome do Paciente", placeholder="Digite o nome do paciente")

    # Obter a lista de pacientes
    pacientes = listar_pacientes()

    if pacientes:
        # Filtrar pacientes pelo nome, se o filtro estiver preenchido
        if filtro_nome:
            pacientes = [p for p in pacientes if filtro_nome.lower() in p["nome"].lower()]

        # Ordenar a lista alfabeticamente pelo nome
        pacientes = sorted(pacientes, key=lambda x: x["nome"].lower())

        # Exibir os pacientes filtrados e ordenados
        if pacientes:
            for paciente in pacientes:
                st.subheader(f"Paciente: {paciente['nome']}")
                st.write(f"CPF: {paciente['cpf']}")
                st.write(f"Telefone: {paciente['telefone']}")
                st.write(f"E-mail: {paciente['email']}")
                st.write(f"Endereço: {paciente['endereco']}")
                st.write(f"Observação: {paciente['observacao']}")
                st.write("---")
        else:
            st.warning("Nenhum paciente encontrado com esse nome.")
    else:
        st.warning("Não há pacientes cadastrados.")

# Executar a página
if __name__ == "__main__":
    listar_pacientes_page()
