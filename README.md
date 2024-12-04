# **Dashboard para Monitoramento de Pacientes**

Um sistema integrado que auxilia psicólogos a monitorar pacientes durante sessões de terapia expositiva. O projeto utiliza **FastAPI** no backend e **Streamlit** no frontend para fornecer um dashboard interativo e em tempo real.

---

## **Índice**
- [Visão Geral](#visão-geral)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Como Executar](#como-executar)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuições](#contribuições)
- [Licença](#licença)

---

## **Visão Geral**
Este sistema foi desenvolvido para auxiliar psicólogos durante sessões de terapia ao:
1. Cadastrar e gerenciar pacientes e psicólogos.
2. Monitorar dados em tempo real, como frequência cardíaca (BPM).
3. Exibir informações relevantes do paciente, como tipo de medo, idade e observações médicas.

---

## **Funcionalidades**
- **Backend**:
  - Cadastro de pacientes e psicólogos.
  - Relacionamento entre pacientes e seus medos.
  - Endpoints RESTful para gerenciamento de dados.

- **Frontend**:
  - Páginas para cadastro e listagem de pacientes e psicólogos.
  - Tela de visualização de dados em tempo real, com atualizações dinâmicas.
  
---

## **Tecnologias Utilizadas**
- **Backend**:
  - [FastAPI](https://fastapi.tiangolo.com/): Framework para APIs RESTful.
  - **SQLAlchemy**: ORM para manipulação do banco de dados.
  - **Alembic**: Gerenciamento de migrações do banco de dados.

- **Frontend**:
  - [Streamlit](https://streamlit.io/): Framework para criação de interfaces de dados.
  - **Requests**: Para comunicação entre frontend e backend.

---

## **Instalação**
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Configure ambientes virtuais:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   pip install -r frontend/requirements.txt
   ```

---

## **Configuração**
### **Backend**
1. Crie o banco de dados:
   - O projeto utiliza SQLite como padrão (arquivo `fabrica.db`).
   - Para criar o banco e aplicar migrações:
     ```bash
     cd backend
     alembic upgrade head
     ```

2. Configure o arquivo `.env` no diretório do backend:
   ```env
   DATABASE_URL=sqlite:///fabrica.db
   ```

### **Frontend**
1. Certifique-se de que o arquivo `.env` no diretório do frontend contém a URL da API:
   ```env
   API_BASE_URL=http://localhost:8000
   ```


## **Como Executar**
1. Inicie o backend:
   ```bash
   uvicorn backend.src.main:app --reload
   ```




2. Inicie o frontend:
   ```bash
   streamlit run frontend/app/streamlit_app.py
   ```



3. Acesse o frontend em: [http://localhost:8501](http://localhost:8501)

---

## **Estrutura do Projeto**

```
├── backend/
│   ├── alembic/           # Controle de migrações do banco de dados
│   ├── src/
│   │   ├── components/
│   │   │   ├── models/    # Modelos das tabelas (Paciente, Medo, etc.)
│   │   │   ├── services/  # Regras de negócio
│   │   └── routers/       # Endpoints RESTful
│   ├── utils/             # Funções auxiliares
│   └── main.py            # Ponto de entrada da API
├── frontend/
│   ├── app/
│   │   ├── controllers/   # Comunicação com o backend
│   │   ├── pages/         # Páginas do frontend
│   │   ├── assets/        # Estilos (CSS) e recursos visuais
│   │   └── streamlit_app.py # Ponto de entrada do Streamlit
├── .env                   # Configurações de ambiente
├── README.md              # Documentação do projeto
├── fabrica.db             # Banco de dados SQLite
```

---



docker build -t my_fastapi_backend .
docker run -d -p 8000:8000 my_fastapi_backend
