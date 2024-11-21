import streamlit as st
import pandas as pd
import requests
from datetime import date
from controllers.consulta_controller import criar_consulta, listar_consultas

# Função para listar pacientes e psicólogos
def listar_pacientes():
    response = requests.get("http://localhost:8000/pacientes/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao carregar pacientes.")
        return []

def listar_psicologos():
    response = requests.get("http://localhost:8000/psicologos/")
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Erro ao carregar psicólogos.")
        return []

def consultas_page():
    st.title("Cadastro de Consultas")

    # Formulário para cadastro de consulta
    with st.form("form_consulta"):
        st.subheader("Nova Consulta")

        # Carrega pacientes e psicólogos para seleção
        pacientes = listar_pacientes()
        psicologos = listar_psicologos()

        paciente_names = [paciente['nome'] for paciente in pacientes]
        psicologo_names = [psicologo['nome'] for psicologo in psicologos]

        nome_paciente = st.selectbox("Selecione o Paciente", paciente_names)
        nome_psicologo = st.selectbox("Selecione o Psicólogo", psicologo_names)

        # Encontre os IDs do paciente e psicólogo selecionado
        paciente_id = next(paciente['id_paciente'] for paciente in pacientes if paciente['nome'] == nome_paciente)
        psicologo_id = next(psicologo['id_psicologo'] for psicologo in psicologos if psicologo['nome'] == nome_psicologo)

        # Seletor de data com intervalo de hoje até 2030
        data_consulta = st.date_input(
            "Data da Consulta",
            min_value=date.today(),  # Data mínima é o dia de hoje
            max_value=date(2030, 12, 31),  # Data máxima é 31 de dezembro de 2030
            help="Escolha a data da consulta"
        )

        # Botão de submissão
        submitted = st.form_submit_button("Cadastrar Consulta")
        if submitted:
            try:
                consulta_data = {
                    "id_paciente": paciente_id,
                    "id_psicologo": psicologo_id,
                    "data_consulta": str(data_consulta),  # Convertendo a data selecionada para string
                }
                nova_consulta = criar_consulta(consulta_data)
                st.success(f"Consulta cadastrada com sucesso! ID: {nova_consulta['id_consulta']}")
            except Exception as e:
                st.error(f"Erro ao cadastrar consulta: {e}")

    # Listagem de consultas cadastradas
    st.subheader("Consultas Cadastradas")

    try:
        consultas = listar_consultas()
        if consultas:
            # Exibir filtros para consulta
            st.subheader("Filtrar Consultas")

            # Filtros
            paciente_filter = st.selectbox("Filtrar por Paciente", ["Todos"] + paciente_names)
            psicologo_filter = st.selectbox("Filtrar por Psicólogo", ["Todos"] + psicologo_names)

            # Adicionando a opção "Todos" ao filtro de data
            data_consultas = [consulta['data_consulta'] for consulta in consultas]
            datas_unicas = sorted(set(data_consultas))  # Datas únicas para filtrar
            datas_unicas.insert(0, "Todos")  # Adiciona a opção "Todos"

            data_filter = st.selectbox("Filtrar por Data", datas_unicas)

            # Aplica os filtros ao DataFrame de consultas
            consulta_data = []
            for consulta in consultas:
                paciente_nome = next(paciente['nome'] for paciente in pacientes if paciente['id_paciente'] == consulta['id_paciente'])
                psicologo_nome = next(psicologo['nome'] for psicologo in psicologos if psicologo['id_psicologo'] == consulta['id_psicologo'])
                consulta_data.append({
                    "Data": consulta['data_consulta'],
                    "Paciente": paciente_nome,
                    "Psicólogo": psicologo_nome
                })

            df_consultas = pd.DataFrame(consulta_data)

            # Aplicando os filtros
            if paciente_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Paciente'] == paciente_filter]
            if psicologo_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Psicólogo'] == psicologo_filter]
            if data_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Data'] == data_filter]

            # Exibindo a tabela com as consultas filtradas
            if not df_consultas.empty:
                st.dataframe(df_consultas)  # Exibindo a tabela de consultas filtradas
            else:
                st.info("Nenhuma consulta encontrada com os filtros selecionados.")

            # Contagem de pacientes por psicólogo
            st.subheader("Contagem de Pacientes por Psicólogo")
            psicologo_counts = df_consultas['Psicólogo'].value_counts().reset_index()
            psicologo_counts.columns = ['Psicólogo', 'Número de Pacientes']

            # Ordenando de forma decrescente pela quantidade de pacientes
            psicologo_counts = psicologo_counts.sort_values(by='Número de Pacientes', ascending=False)

            # Exibindo a tabela de contagem de pacientes
            st.dataframe(psicologo_counts)

        else:
            st.info("Nenhuma consulta cadastrada.")
    except Exception as e:
        st.error(f"Erro ao carregar consultas: {e}")
