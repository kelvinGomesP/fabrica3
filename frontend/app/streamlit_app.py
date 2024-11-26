import os
import streamlit as st
from pages.cadastro_paciente import cadastro_paciente
from pages.cadastro_psicologo import cadastro_psicologo
from pages.tempo_real import visualizar_paciente
from pages.consultas_page import consultas_page

# Função para obter o caminho de imagens
def get_image_path(image_name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_path, "images", image_name)
    return image_path

# Navegação entre páginas
def navigate_to(page_name):
    st.experimental_set_query_params(page=page_name)

# Configuração inicial
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

# Obter a página atual
query_params = st.query_params
current_page = query_params.get("page", ["home"])[0]

# Caminhos das imagens
brain_image_path = get_image_path("mente1.jpg")
logo_image_path = get_image_path("idp_logo.png")

# Renderizar as páginas
if current_page == "home":
    st.title("Bem-vindo ao Dashboard de Psicologia 🧠")
    if os.path.exists(brain_image_path):
        st.image(brain_image_path, caption="Explorando a mente humana")
    else:
        st.error("Erro: Imagem da mente não encontrada.")

    st.subheader("Transformando dados em insights para a saúde mental")
    st.markdown(
        """
        Este dashboard é uma ferramenta integrada para monitoramento de pacientes em tempo real, 
        gerenciamento de consultas e análise de dados clínicos.
        """
    )
    st.markdown("---")
    if os.path.exists(logo_image_path):
        st.image(logo_image_path, width=200)
    else:
        st.error("Erro: Logo do IDP não encontrada.")

    # Botões de navegação
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        if st.button("📊 Monitoramento em Tempo Real"):
            navigate_to("tempo_real")
            st.experimental_rerun()
    with col2:
        if st.button("👤 Cadastro de Pacientes"):
            navigate_to("cadastro_paciente")
            st.experimental_rerun()
    with col3:
        if st.button("👨‍⚕️ Cadastro Psicólogo"):
            navigate_to("cadastro_psicologo")
            st.experimental_rerun()
    with col4:
        if st.button("📅 Consultas"):
            navigate_to("consultas")
            st.experimental_rerun()

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
