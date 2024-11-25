import streamlit as st
from pages.cadastro_paciente import cadastro_paciente
from pages.cadastro_psicologo import cadastro_psicologo
from pages.tempo_real import visualizar_paciente
from pages.consultas_page import consultas_page

# Configurações iniciais da página
st.set_page_config(
    page_title="Dashboard de Psicologia",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS customizado
st.markdown(
    """
    <style>
        body {
            background: linear-gradient(to bottom right, #2C3E50, #4CA1AF);
            color: white;
        }
        .stButton button {
            background-color: #4CA1AF;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background-color: #3E8E92;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Função para navegação entre páginas
def navigate_to(page_name):
    st.query_params['page'] = page_name

# Obter a página atual da URL
current_page = st.query_params.get("page", "home")

# Renderizar páginas com base no query parameter
if current_page == "home":
    st.title("Bem-vindo ao Dashboard de Psicologia 🧠")
    st.subheader("Transformando dados em insights para a saúde mental")
    st.markdown(
        """
        Este dashboard é uma ferramenta integrada para monitoramento de pacientes em tempo real, 
        gerenciamento de consultas e análise de dados clínicos.
        """
    )

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("📊 Monitoramento em Tempo Real"):
            navigate_to("tempo_real")
            st.rerun()
    with col2:
        if st.button("👤 Cadastro de Pacientes"):
            navigate_to("cadastro_paciente")
            st.rerun()
    with col3:
        if st.button("👨‍⚕️ Cadastro Psicólogo"):
            navigate_to("cadastro_psicologo")
            st.rerun()
    with col4:
        if st.button("📅 Consultas"):
            navigate_to("consultas")
            st.rerun()

elif current_page == "tempo_real":
    visualizar_paciente()

elif current_page == "cadastro_paciente":
    cadastro_paciente()

elif current_page == "cadastro_psicologo":
    cadastro_psicologo()

elif current_page == "consultas":
    consultas_page()

# Rodapé
st.markdown(
    """
    <hr style="border: none; height: 1px; background: #4CA1AF;">
    <p style='text-align: center; font-size: 14px;'>
        Desenvolvido pelo <b>IDP-DF</b> | Fábrica de Projetos 3 | 2024
    </p>
    """,
    unsafe_allow_html=True,
)
