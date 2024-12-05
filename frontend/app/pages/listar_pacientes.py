import streamlit as st
import requests

# URL da API
API_BASE_URL = "http://localhost:8000"

from func.back_to_home import render_back_to_home_button

# Função para buscar pacientes, medos e relações
def fetch_data():
    try:
        with st.spinner("Carregando dados..."):
            pacientes_response = requests.get(f"{API_BASE_URL}/pacientes/")
            pacientes_response.raise_for_status()
            pacientes = pacientes_response.json()

            paciente_medos_response = requests.get(f"{API_BASE_URL}/pacientes-medos/")
            paciente_medos_response.raise_for_status()
            paciente_medos = paciente_medos_response.json()

            medos_response = requests.get(f"{API_BASE_URL}/medos/")
            medos_response.raise_for_status()
            medos = medos_response.json()

        return pacientes, paciente_medos, medos
    except requests.exceptions.RequestException as e:
        st.error(f"Erro ao buscar dados da API: {e}")
        return [], [], []

# Função para combinar os dados de pacientes com e sem medos
def combinar_dados(pacientes, paciente_medos, medos):
    medo_dict = {medo["id_medo"]: medo for medo in medos}
    pacientes_com_medo = []
    pacientes_sem_medo = set(p["id_paciente"] for p in pacientes)

    for relacao in paciente_medos:
        paciente = next((p for p in pacientes if p["id_paciente"] == relacao["id_paciente"]), None)
        medo = medo_dict.get(relacao["id_medo"], None)

        if paciente and medo:
            pacientes_com_medo.append({
                "Nome": paciente["nome"],
                "Medo": medo["nome_medo"],
                "Grau": medo["grau_medo"],
                "Data de Nascimento": paciente["data_nascimento"],
                "CPF": paciente["cpf"],
                "Telefone": paciente["telefone"],
                "Email": paciente["email"],
                "Endereço": paciente["endereco"],
                "Observação": paciente["observacao"],
            })
            pacientes_sem_medo.discard(paciente["id_paciente"])

    pacientes_sem_medo = [
        {
            "Nome": p["nome"],
            "Medo": "Nenhum",
            "Grau": "N/A",
            "Data de Nascimento": p["data_nascimento"],
            "CPF": p["cpf"],
            "Telefone": p["telefone"],
            "Email": p["email"],
            "Endereço": p["endereco"],
            "Observação": p["observacao"],
        }
        for p in pacientes if p["id_paciente"] in pacientes_sem_medo
    ]

    return pacientes_com_medo, pacientes_sem_medo

# Função para exibir pacientes em cartões
def exibir_pacientes(pacientes, titulo):
    st.subheader(titulo)

    if not pacientes:
        st.info(f"Não há {titulo.lower()} cadastrados.")
        return

    for paciente in pacientes:
        st.markdown(f"""
        <div style="
            border: 1px solid #444; 
            border-radius: 8px; 
            padding: 15px; 
            margin-bottom: 15px; 
            background-color: #333; 
            color: #EEE;
        ">
            <h3 style="color: #FFF; margin-bottom: 10px;">{paciente['Nome']}</h3>
            <p><strong>Medo:</strong> <span style="color: #FF6347;">{paciente['Medo']}</span></p>
            <p><strong>Grau:</strong> {paciente['Grau']}</p>
            <p><strong>Data de Nascimento:</strong> {paciente['Data de Nascimento']}</p>
            <p><strong>CPF:</strong> {paciente['CPF']}</p>
            <p><strong>Telefone:</strong> {paciente['Telefone']}</p>
            <p><strong>Email:</strong> {paciente['Email']}</p>
            <p><strong>Endereço:</strong> {paciente['Endereço']}</p>
            <p><strong>Observação:</strong> {paciente['Observação'] if paciente['Observação'] else "Nenhuma"}</p>
        </div>
        """, unsafe_allow_html=True)

# Página principal
def main():
    render_back_to_home_button()

    # Ajuste do estilo geral
    st.markdown("""
    <style>
        body { background-color: #222; color: #EEE; font-family: 'Arial', sans-serif; }
        h1, h2, h3 { color: #FFF; }
        .stTextInput label, .stSelectbox label { color: #EEE; }
    </style>
    """, unsafe_allow_html=True)

    st.title("Lista de Pacientes e Seus Medos")
    st.markdown("Gerencie e visualize os pacientes e seus respectivos medos de forma organizada.")

    # Buscar dados
    pacientes, paciente_medos, medos = fetch_data()

    if pacientes:
        # Combinar dados
        pacientes_com_medo, pacientes_sem_medo = combinar_dados(pacientes, paciente_medos, medos)

        # Ordena os pacientes por nome
        pacientes_com_medo.sort(key=lambda x: x['Nome'])
        pacientes_sem_medo.sort(key=lambda x: x['Nome'])

        # Filtros
        st.markdown("### Filtros")
        col1, col2 = st.columns(2)
        with col1:
            nome_filtro = st.text_input("Filtrar por nome")
        with col2:
            medo_filtro = st.selectbox("Filtrar por medo", ["Todos"] + [m["nome_medo"] for m in medos])

        # Aplicação dos filtros
        if nome_filtro:
            pacientes_com_medo = [p for p in pacientes_com_medo if nome_filtro.lower() in p["Nome"].lower()]
            pacientes_sem_medo = [p for p in pacientes_sem_medo if nome_filtro.lower() in p["Nome"].lower()]

        if medo_filtro != "Todos":
            pacientes_com_medo = [p for p in pacientes_com_medo if p["Medo"] == medo_filtro]

        # Exibição
        exibir_pacientes(pacientes_com_medo, "Pacientes com Medos")
        exibir_pacientes(pacientes_sem_medo, "Pacientes sem Medos")
    else:
        st.warning("Não foi possível carregar os dados dos pacientes.")

if __name__ == "__main__":
    main()
