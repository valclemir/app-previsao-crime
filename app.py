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

bairros = {
    1: "Centro",
    2: "Junco",
    3: "Dom Expedito",
    4: "Dom José",
    5: "Sinhá Sabóia",
    6: "Alto do Cristo",
    7: "Campo dos Velhos",
    8: "Domingos Olímpio",
    9: "Cidade Doutor Jose Euclides Ferreira Gomes Junior",
    10: "Alto da Brasília",
    11: "Renato Parente",
    12: "Cohab I",
    13: "Zona Rural",
    14: "Padre Palhano",
    15: "Distrito Salgado dos Machados",
    16: "Edmundo Monte Coelho",
    17: "Jatobá",
    18: "Alto Novo",
    19: "Cidade Gerardo Cristino de Menezes",
    20: "Cidade Pedro Mendes Carneiro",
    21: "Alto da Expectativa",
    22: "Distrito Jaibaras",
    23: "Distrito Jordão",
    24: "Pedrinhas",
    25: "Distrito Industrial",
    26: "Sumaré",
    27: "Doutor Juvêncio de Andrade",
    28: "Padre Ibiapina",
    29: "Cohab II",
    30: "Colina Boa Vista",
    31: "Das Nações",
    32: "Nossa Senhora de Fátima",
    33: "Nova Caiçara",
    34: "Várzea Grande",
    35: "Coração de Jesus",
    36: "Distritio Aracatiaçu",
    37: "Expectativa",
    38: "Jocely Dantas de Andrade Torres",
    39: "Antonio Carlos Belchior",
    40: "Bairro Pedrinhas",
    41: "Jerônimo de Medeiros Prado",
    42: "Avenida John Sanford",
    43: "Avenida Mãe Rainha",
    44: "Derby Clube",
    45: "Distrito Baracho",
    46: "Distrito de Aprazível",
    47: "Distrito de Caioca",
    48: "Distrito de Jaibaras",
    49: "Distrito de Rafael Arruda",
    50: "Distrito de Salgados do Machados",
    51: "Distrito Patos",
    52: "Distrito Salgado dos Mendes",
    53: "Dom Peixoto",
    54: "Parque Silvana",
    55: "Santa Casa",
    56: "Terrenos Novos",
    57: "Vila Sonia",
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
BAIRRO = st.sidebar.selectbox("Bairro", list(bairros.values()))
ZONA = st.sidebar.selectbox("Zona", ["1", "2", "3", "4", "5"])

# Botão de submissão
if st.button("Submeter"):
    # Converter valores para numéricos
    NATZ_value = ["Pessoa", "Veículo Carro", "Veículo Moto", "Outros", "Residência"].index(NATZ) + 1
    DIASEM_value = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Fim de Semana", "Feriado"].index(DIASEM) + 1
    TIPDIA_value = ["Útil", "Não Útil"].index(TIPDIA) + 1
    FASEMÊS_value = ["F1 (1 a 7)", "F2 (8 a 15)", "F3 (16 a 24)", "F4 (25 a 31)"].index(FASEMÊS) + 1
    TPMÊS_value = ["Férias 1 (Jan, Fev)", "Trimestre 1 (Mar, Abr, Mai)", "São João (Jun)", "Férias 2 (Jul, Ago)", "Trimestre 2 (Set, Out, Nov)", "Férias 3 (Dez)"].index(TPMÊS) + 1
    TPHORA_value = ["Início da Manhã", "Fim da Manhã", "Início da Tarde", "Fim da Tarde", "Início da Noite", "Fim da Noite", "Madrugada"].index(TPHORA) + 1
    BAIRRO_value = list(bairros.keys())[list(bairros.values()).index(BAIRRO)]
    ZONA_value = int(ZONA)

    # Previsão
    input_data = np.array([[NATZ_value, DIASEM_value, TIPDIA_value, FASEMÊS_value, TPMÊS_value, TPHORA_value, BAIRRO_value, ZONA_value]])
    prediction = model.predict(input_data)[0]

    # Exibir resultado
    if prediction == 1:
        st.error("Resultado: Crime")
    else:
        st.success("Resultado: Não Crime")