import streamlit as st
import pandas as pd
import requests
from datetime import date
from controllers.consulta_controller import criar_consulta, listar_consultas
from func.back_to_home import render_back_to_home_button


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
    render_back_to_home_button()
    st.title("Cadastro de Consultas")
    st.markdown("### Preencha os dados abaixo para cadastrar uma nova consulta.")

    # Formulário para cadastro de consulta
    with st.form("form_consulta"):
        # Carrega pacientes e psicólogos para seleção
        with st.spinner("Carregando pacientes e psicólogos..."):
            pacientes = listar_pacientes()
            psicologos = listar_psicologos()

        if not pacientes or not psicologos:
            st.warning("Não foi possível carregar os dados de pacientes ou psicólogos.")
            return

        paciente_names = [paciente['nome'] for paciente in pacientes]
        psicologo_names = [psicologo['nome'] for psicologo in psicologos]

        col1, col2 = st.columns(2)
        with col1:
            nome_paciente = st.selectbox("Paciente", paciente_names)
        with col2:
            nome_psicologo = st.selectbox("Psicólogo", psicologo_names)

        # Obter IDs dos selecionados
        paciente_id = next(p['id_paciente'] for p in pacientes if p['nome'] == nome_paciente)
        psicologo_id = next(p['id_psicologo'] for p in psicologos if p['nome'] == nome_psicologo)

        data_consulta = st.date_input(
            "Data da Consulta",
            min_value=date.today(),
            max_value=date(2030, 12, 31),
            help="Selecione uma data entre hoje e 31/12/2030."
        )

        submitted = st.form_submit_button("Cadastrar Consulta")
        if submitted:
            try:
                consulta_data = {
                    "id_paciente": paciente_id,
                    "id_psicologo": psicologo_id,
                    "data_consulta": str(data_consulta),
                }
                nova_consulta = criar_consulta(consulta_data)
                st.success(f"Consulta cadastrada com sucesso! ID: {nova_consulta['id_consulta']}")
            except Exception as e:
                st.error(f"Erro ao cadastrar consulta: {e}")

    st.markdown("---")
    st.subheader("Consultas Cadastradas")

    # Carregamento e filtros
    try:
        consultas = listar_consultas()
        if consultas:
            # Estrutura da tabela
            consulta_data = []
            for consulta in consultas:
                paciente_nome = next(p['nome'] for p in pacientes if p['id_paciente'] == consulta['id_paciente'])
                psicologo_nome = next(p['nome'] for p in psicologos if p['id_psicologo'] == consulta['id_psicologo'])
                consulta_data.append({
                    "Data": consulta['data_consulta'],
                    "Paciente": paciente_nome,
                    "Psicólogo": psicologo_nome,
                })

            df_consultas = pd.DataFrame(consulta_data)

            # Filtros
            st.markdown("#### Filtros")
            col1, col2, col3 = st.columns(3)
            with col1:
                paciente_filter = st.selectbox("Por Paciente", ["Todos"] + paciente_names)
            with col2:
                psicologo_filter = st.selectbox("Por Psicólogo", ["Todos"] + psicologo_names)
            with col3:
                data_filter = st.selectbox("Por Data", ["Todos"] + sorted(df_consultas["Data"].unique()))

            if paciente_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Paciente'] == paciente_filter]
            if psicologo_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Psicólogo'] == psicologo_filter]
            if data_filter != "Todos":
                df_consultas = df_consultas[df_consultas['Data'] == data_filter]

            # Exibição da tabela
            if not df_consultas.empty:
                st.dataframe(df_consultas, use_container_width=True)
                st.download_button(
                    label="Baixar tabela como CSV",
                    data=df_consultas.to_csv(index=False),
                    file_name="consultas.csv",
                    mime="text/csv"
                )
            else:
                st.info("Nenhuma consulta encontrada com os filtros aplicados.")

        else:
            st.info("Nenhuma consulta cadastrada.")
    except Exception as e:
        st.error(f"Erro ao carregar consultas: {e}")


# Executar a página
if __name__ == "__main__":
    consultas_page()
