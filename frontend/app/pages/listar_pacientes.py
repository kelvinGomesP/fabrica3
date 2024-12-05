import streamlit as st
import requests

# URL da API
API_BASE_URL = "http://localhost:8000"

from func.back_to_home import render_back_to_home_button

# Função para buscar pacientes, medos e relações
def fetch_data():
    try:
        pacientes_response = requests.get(f"{API_BASE_URL}/pacientes/")
        pacientes_response.raise_for_status()
        pacientes = pacientes_response.json()

        paciente_medos_response = requests.get(f"{API_BASE_URL}/pacientes-medos/")
        paciente_medos_response.raise_for_status()
        paciente_medos = paciente_medos_response.json()

        medos_response = requests.get(f"{API_BASE_URL}/medos/")  # Obter medos
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

# Função para estilizar a exibição de pacientes
def exibir_pacientes(pacientes, titulo):
    st.subheader(titulo)

    if not pacientes:
        st.warning(f"Não há {titulo.lower()} cadastrados.")
        return

    for paciente in pacientes:
        st.markdown(f"""
        <div style="border: 1px solid #ccc; border-radius: 10px; padding: 15px; margin-bottom: 20px; background-color: #696969;">
            <h2 style="color: #007BFF; margin-bottom: 10px;">{paciente['Nome']}</h2>
            <p><strong>Medo:</strong> <span style="color: #FF6347;">{paciente['Medo']}</span></p>
            <ul style="list-style-type: none; padding: 0; margin-top: 10px;">
                <li><strong>Grau:</strong> {paciente['Grau']}</li>
                <li><strong>Data de Nascimento:</strong> {paciente['Data de Nascimento']}</li>
                <li><strong>CPF:</strong> {paciente['CPF']}</li>
                <li><strong>Telefone:</strong> {paciente['Telefone']}</li>
                <li><strong>Email:</strong> {paciente['Email']}</li>
                <li><strong>Endereço:</strong> {paciente['Endereço']}</li>
                <li><strong>Observação:</strong> {paciente['Observação'] if paciente['Observação'] else "Nenhuma"}</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# Página principal
def main():
    render_back_to_home_button()
    # Define um fundo cinza claro para a página
    st.markdown("""<style>body { background-color: #696969; }</style>""", unsafe_allow_html=True)

    st.title("Lista de Pacientes e Seus Medos")

    # Buscar dados
    pacientes, paciente_medos, medos = fetch_data()

    if pacientes:
        # Combinar dados
        pacientes_com_medo, pacientes_sem_medo = combinar_dados(pacientes, paciente_medos, medos)

        # Ordena os pacientes por nome
        pacientes_com_medo.sort(key=lambda x: x['Nome'])
        pacientes_sem_medo.sort(key=lambda x: x['Nome'])

        # Filtro de nome do paciente
        nome_filtro = st.text_input("Filtrar por nome do paciente")

        # Filtro de medo
        medos_lista = [medo["nome_medo"] for medo in medos]
        medo_filtro = st.selectbox("Filtrar por medo", ["Todos"] + medos_lista)

        # Filtrar os pacientes com base nos filtros
        if nome_filtro:
            pacientes_com_medo = [p for p in pacientes_com_medo if nome_filtro.lower() in p["Nome"].lower()]
            pacientes_sem_medo = [p for p in pacientes_sem_medo if nome_filtro.lower() in p["Nome"].lower()]

        if medo_filtro != "Todos":
            pacientes_com_medo = [p for p in pacientes_com_medo if p["Medo"] == medo_filtro]

        # Exibir pacientes com medos
        exibir_pacientes(pacientes_com_medo, "Pacientes com Medos")

        # Exibir pacientes sem medos
        exibir_pacientes(pacientes_sem_medo, "Pacientes sem Medos")
    else:
        st.warning("Não foi possível carregar os dados dos pacientes.")

if __name__ == "__main__":
    main()
