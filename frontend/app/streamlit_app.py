# Atualização do primeiro código: streamlit_app.py
import os
import streamlit as st
from pages.cadastro_paciente import cadastro_paciente
from pages.cadastro_psicologo import cadastro_psicologo
from pages.tempo_real import visualizar_paciente
from pages.consultas_page import consultas_page
from pages.listar_pacientes import main as listar_pacientes

# Função para obter o caminho de imagens
def get_image_path(image_name):
    current_path = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_path, "images", image_name)
    return image_path

# Navegação entre páginas
def navigate_to(page_name):
    st.query_params = {"page": page_name}

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
        .full-width-image img {
            display: block;
            width: 100%;
            height: auto;
            margin: 0 auto;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Obter a página atual
query_params = st.query_params
current_page = query_params.get("page", "home")

# Caminhos das imagens
brain_image_path = get_image_path("mente1.jpg")
logo_image_path = get_image_path("idp_logo.png")

# Renderizar as páginas
if current_page == "home":
    st.title("Bem-vindo ao Dashboard de Psicologia 🧠")
    if os.path.exists(brain_image_path):
        st.markdown(
            f"<div class='full-width-image'><img src='data:image/jpeg;base64,{st.image(brain_image_path, use_column_width=True)}' alt=''></div>",
            unsafe_allow_html=True,
        )
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

    # Botões de navegação
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        if st.button("📈 Monitoramento em Tempo Real"):
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
    with col5:
        if st.button("🔍 Listar Pacientes"):
            navigate_to("listar_pacientes")
            st.rerun()

elif current_page == "tempo_real":
    visualizar_paciente()

elif current_page == "cadastro_paciente":
    cadastro_paciente()

elif current_page == "cadastro_psicologo":
    cadastro_psicologo()

elif current_page == "consultas":
    consultas_page()

elif current_page == "listar_pacientes":
    listar_pacientes()

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
