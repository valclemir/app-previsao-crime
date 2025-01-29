import streamlit as st
import numpy as np
import joblib  # Para carregar o modelo salvo

# Carregar o modelo treinado
# Certifique-se de que o modelo salvo esteja no mesmo diretório, ou ajuste o caminho
model = joblib.load("model-catboost-violencia.pkl")  # Substitua pelo nome do arquivo do modelo salvo

# Dicionários de Conversão
natureza_roubo = {
    1: "Pessoa",
    2: "Veículo Carro",
    3: "Veículo Moto",
    4: "Outros",
    5: "Residência"
}

dia_semana = {
    1: "Segunda-feira",
    2: "Terça-feira",
    3: "Quarta-feira",
    4: "Quinta-feira",
    5: "Sexta-feira",
    6: "Fim de Semana",
    7: "Feriado"
}

tipo_dia = {
    1: "Útil",
    2: "Não Útil"
}

fase_mes = {
    1: "F1 (1 a 7)",
    2: "F2 (8 a 15)",
    3: "F3 (16 a 24)",
    4: "F4 (25 a 31)"
}

tipo_mes = {
    1: "Férias 1 (Jan, Fev)",
    2: "Trimestre 1 (Mar, Abr, Mai)",
    3: "São João (Jun)",
    4: "Férias 2 (Jul, Ago)",
    5: "Trimestre 2 (Set, Out, Nov)",
    6: "Férias 3 (Dez)"
}

tipo_horario = {
    1: "Início da Manhã",
    2: "Fim da Manhã",
    3: "Início da Tarde",
    4: "Fim da Tarde",
    5: "Início da Noite",
    6: "Fim da Noite",
    7: "Madrugada"
}

bairro_data = {
    "Alto da Expectativa": {"CD_BAIRRO": 21, "ZONA": 1},
    "Alto do Cristo": {"CD_BAIRRO": 6, "ZONA": 1},
    "Alto Novo": {"CD_BAIRRO": 18, "ZONA": 1},
    "Bairro Pedrinhas": {"CD_BAIRRO": 40, "ZONA": 1},
    "Campo dos Velhos": {"CD_BAIRRO": 7, "ZONA": 1},
    "Centro": {"CD_BAIRRO": 1, "ZONA": 1},
    "Coração de Jesus": {"CD_BAIRRO": 35, "ZONA": 1},
    "Domingos Olímpio": {"CD_BAIRRO": 8, "ZONA": 1},
    "Expectativa": {"CD_BAIRRO": 37, "ZONA": 1},
    "Padre Ibiapina": {"CD_BAIRRO": 28, "ZONA": 1},
    "Parque Silvana": {"CD_BAIRRO": 54, "ZONA": 1},
    "Pedrinhas": {"CD_BAIRRO": 24, "ZONA": 1},
    "Santa Casa": {"CD_BAIRRO": 55, "ZONA": 1},
    "Antonio Carlos Belchior": {"CD_BAIRRO": 39, "ZONA": 2},
    "Cidade Gerardo Cristino de Menezes": {"CD_BAIRRO": 19, "ZONA": 2},
    "Cohab I": {"CD_BAIRRO": 12, "ZONA": 2},
    "Cohab II": {"CD_BAIRRO": 29, "ZONA": 2},
    "Das Nações": {"CD_BAIRRO": 31, "ZONA": 2},
    "Derby Clube": {"CD_BAIRRO": 44, "ZONA": 2},
    "Distrito Industrial": {"CD_BAIRRO": 25, "ZONA": 2},
    "Distrito Salgado dos Machados": {"CD_BAIRRO": 15, "ZONA": 2},
    "Dom Expedito": {"CD_BAIRRO": 3, "ZONA": 2},
    "Jatobá": {"CD_BAIRRO": 17, "ZONA": 2},
    "Sinhá Sabóia": {"CD_BAIRRO": 5, "ZONA": 2},
    "Várzea Grande": {"CD_BAIRRO": 34, "ZONA": 2},
    "Avenida John Sanford": {"CD_BAIRRO": 42, "ZONA": 3},
    "Avenida Mãe Rainha": {"CD_BAIRRO": 43, "ZONA": 3},
    "Cidade Doutor Jose Euclides Ferreira Gomes Junior": {"CD_BAIRRO": 9, "ZONA": 3},
    "Colina Boa Vista": {"CD_BAIRRO": 30, "ZONA": 3},
    "Dom José": {"CD_BAIRRO": 4, "ZONA": 3},
    "Dom Peixoto": {"CD_BAIRRO": 53, "ZONA": 3},
    "Edmundo Monte Coelho": {"CD_BAIRRO": 16, "ZONA": 3},
    "Junco": {"CD_BAIRRO": 2, "ZONA": 3},
    "Nossa Senhora de Fátima": {"CD_BAIRRO": 32, "ZONA": 3},
    "Nova Caiçara": {"CD_BAIRRO": 33, "ZONA": 3},
    "Padre Palhano": {"CD_BAIRRO": 14, "ZONA": 3},
    "Renato Parente": {"CD_BAIRRO": 11, "ZONA": 3},
    "Sumaré": {"CD_BAIRRO": 26, "ZONA": 3},
    "Alto da Brasília": {"CD_BAIRRO": 10, "ZONA": 4},
    "Cidade Pedro Mendes Carneiro": {"CD_BAIRRO": 20, "ZONA": 4},
    "Doutor Juvêncio de Andrade": {"CD_BAIRRO": 27, "ZONA": 4},
    "Jerônimo de Medeiros Prado": {"CD_BAIRRO": 41, "ZONA": 4},
    "Jocely Dantas de Andrade Torres": {"CD_BAIRRO": 38, "ZONA": 4},
    "Vila Sonia": {"CD_BAIRRO": 57, "ZONA": 4},
    "Distritio Aracatiaçu": {"CD_BAIRRO": 36, "ZONA": 5},
    "Distrito Baracho": {"CD_BAIRRO": 45, "ZONA": 5},
    "Distrito de Aprazível": {"CD_BAIRRO": 46, "ZONA": 5},
    "Distrito de Caioca": {"CD_BAIRRO": 47, "ZONA": 5},
    "Distrito de Jaibaras": {"CD_BAIRRO": 48, "ZONA": 5},
    "Distrito de Rafael Arruda": {"CD_BAIRRO": 49, "ZONA": 5},
    "Distrito de Salgados do Machados": {"CD_BAIRRO": 50, "ZONA": 5},
    "Distrito Jaibaras": {"CD_BAIRRO": 22, "ZONA": 5},
    "Distrito Jordão": {"CD_BAIRRO": 23, "ZONA": 5},
    "Distrito Patos": {"CD_BAIRRO": 51, "ZONA": 5},
    "Distrito Salgado dos Mendes": {"CD_BAIRRO": 52, "ZONA": 5},
    "Terrenos Novos": {"CD_BAIRRO": 56, "ZONA": 5},
    "Zona Rural": {"CD_BAIRRO": 13, "ZONA": 5},
}

# App Streamlit
st.title("Previsão de Crime")

# Entrada do usuário
st.sidebar.header("Insira os dados do caso")
NATZ = st.sidebar.selectbox("Natureza do Roubo", ["Pessoa", "Veículo Carro", "Veículo Moto", "Outros", "Residência"])
DIASEM = st.sidebar.selectbox("Dia da Semana", ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Fim de Semana", "Feriado"])
TIPDIA = st.sidebar.selectbox("Tipo do Dia", ["Útil", "Não Útil"])
FASEMÊS = st.sidebar.selectbox("Fase do Mês", ["F1 (1 a 7)", "F2 (8 a 15)", "F3 (16 a 24)", "F4 (25 a 31)"])
TPMÊS = st.sidebar.selectbox("Tipo do Mês", ["Férias 1 (Jan, Fev)", "Trimestre 1 (Mar, Abr, Mai)", "São João (Jun)", "Férias 2 (Jul, Ago)", "Trimestre 2 (Set, Out, Nov)", "Férias 3 (Dez)"])
TPHORA = st.sidebar.selectbox("Tipo de Horário", ["Início da Manhã", "Fim da Manhã", "Início da Tarde", "Fim da Tarde", "Início da Noite", "Fim da Noite", "Madrugada"])
BAIRRO = st.sidebar.selectbox("Bairro", list(bairro_data.keys()))

# Preenchimento automático do ID do bairro e da zona
CD_BAIRRO = bairro_data[BAIRRO]["CD_BAIRRO"]
ZONA = bairro_data[BAIRRO]["ZONA"]

# Exibir zona e ID automaticamente
st.sidebar.text(f"Zona selecionada: {ZONA}")

# Botão de submissão
if st.button("Submeter"):
    # Converter valores para numéricos
    NATZ_value = ["Pessoa", "Veículo Carro", "Veículo Moto", "Outros", "Residência"].index(NATZ) + 1
    DIASEM_value = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Fim de Semana", "Feriado"].index(DIASEM) + 1
    TIPDIA_value = ["Útil", "Não Útil"].index(TIPDIA) + 1
    FASEMÊS_value = ["F1 (1 a 7)", "F2 (8 a 15)", "F3 (16 a 24)", "F4 (25 a 31)"].index(FASEMÊS) + 1
    TPMÊS_value = ["Férias 1 (Jan, Fev)", "Trimestre 1 (Mar, Abr, Mai)", "São João (Jun)", "Férias 2 (Jul, Ago)", "Trimestre 2 (Set, Out, Nov)", "Férias 3 (Dez)"].index(TPMÊS) + 1
    TPHORA_value = ["Início da Manhã", "Fim da Manhã", "Início da Tarde", "Fim da Tarde", "Início da Noite", "Fim da Noite", "Madrugada"].index(TPHORA) + 1

    # Previsão
    input_data = np.array([[NATZ_value, DIASEM_value, TIPDIA_value, FASEMÊS_value, TPMÊS_value, TPHORA_value, CD_BAIRRO, ZONA]])
    prediction = model.predict(input_data)[0]

    # Exibir resultado
    if prediction == 1:
        st.error("Resultado: Crime")
    else:
        st.success("Resultado: Não Crime")