import streamlit as st
import time
import requests
from datetime import date, datetime
from controllers.paciente_controller import listar_pacientes
import plotly.graph_objs as go

API_BASE_URL = "http://localhost:8000"

# Função para simular dados de BPM
def obter_bpm_simulado():
    import random
    return random.randint(60, 100)  # Simula valores de BPM entre 60 e 100

# Função para calcular idade a partir da data de nascimento
def calcular_idade(data_nascimento):
    nascimento = datetime.strptime(data_nascimento, "%Y-%m-%d").date()
    hoje = date.today()
    return hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

# Página principal
def visualizar_paciente():
    st.title("Visualização de Dados em Tempo Real")
    st.subheader("Selecione o paciente para monitoramento")

    # Listar pacientes disponíveis
    pacientes = listar_pacientes()
    if not pacientes:
        st.error("Nenhum paciente cadastrado.")
        return

    # Dropdown para seleção de paciente
    nomes_pacientes = {paciente["nome"]: paciente for paciente in pacientes}
    nome_selecionado = st.selectbox("Escolha um paciente:", list(nomes_pacientes.keys()))
    duracao_sessao = st.number_input(
    "Digite a duração da sessão em segundos:",
    min_value=5,
    max_value=180,
    value=30,
    step=10,
    help="Escolha a duração da sessão de monitoramento (entre 10 segundos e 1 hora)."
)

    # Botão de confirmação
    if st.button("Confirmar Seleção"):
        # Recuperar dados do paciente selecionado
        paciente = nomes_pacientes[nome_selecionado]
        idade = calcular_idade(paciente["data_nascimento"])
        medo = paciente.get("medo", {})
        media_bpm = obter_bpm_simulado()  # Em produção, use dados reais
        observacoes = paciente.get("observacao", "Sem observações")

        # Layout em colunas
        col1, col2 = st.columns([2, 1])

        # Informações relevantes do paciente
        with col2:
            st.markdown("### Informações do Paciente")
            st.write(f"**Nome:** {paciente['nome']}")
            st.write(f"**Idade:** {idade} anos")
            st.write(f"**Média de BPM:** {media_bpm}")
            st.write(f"**Tipo de Medo:** {medo.get('nome_medo', 'Sem medo registrado')}")
            st.write(f"**Observações Médicas:** {observacoes}")
            
        # Exibição do BPM em tempo real
        with col1:
            st.markdown("### 🫀 Frequência Cardíaca (BPM)")
            bpm_placeholder = st.empty()
            grafico_placeholder = st.empty()

            # Lista para armazenar dados do BPM
            bpm_dados = []
            tempo = []

            # Configuração inicial do gráfico
            fig = go.Figure()
            fig.update_layout(
                title="Frequência Cardíaca ao Longo do Tempo",
                xaxis_title="Tempo (s)",
                yaxis_title="BPM",
                yaxis=dict(range=[50, 110]),
                template="plotly_dark",
                margin=dict(l=40, r=40, t=40, b=40),
                height=300,
            )

            # Variável de controle para pausa
            pausar_visualizacao = st.button("Pausar Visualização")
            # Atualizar dados de BPM em tempo real
            i = -1
            while(i != duracao_sessao*60):
                if pausar_visualizacao:
                    st.warning("Visualização pausada. Desmarque a opção para continuar.")
                    break

                bpm_atual = obter_bpm_simulado()
                bpm_dados.append(bpm_atual)
                tempo.append(i)  # Incrementa o tempo em segundos
                i += 1
                # Definir cor com base nos valores
                if bpm_atual < 70:
                    cor = "green"
                elif bpm_atual < 90:
                    cor = "orange"
                else:
                    cor = "red"

                bpm_placeholder.markdown(
                    f"""
                    <div style="text-align: center; font-size: 50px; font-weight: bold; color: {cor};">
                        {bpm_atual} BPM
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Atualizar gráfico com Plotly
                fig.data = []  # Limpar dados antigos
                fig.add_trace(go.Scatter(x=tempo, y=bpm_dados, mode="lines+markers", line=dict(color="cyan")))
                grafico_placeholder.plotly_chart(fig, use_container_width=True)

                time.sleep(1)  # Atualiza a cada 1 segundo


# Executar a página
if __name__ == "__main__":
    visualizar_paciente()
