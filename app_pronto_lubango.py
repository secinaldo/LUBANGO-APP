
import streamlit as st
import random

# --- Dados fixos ---
POPULACAO_LUBANGO = 776_249
NOME_MUNICIPIO = "Lubango"

# --- Lista para armazenar terrenos ---
if "terrenos" not in st.session_state:
    st.session_state.terrenos = []

# --- Função de planejamento urbano ---
def calcular_servicos(moradores):
    return {
        "Educação": {
            "Escolas": moradores // 1000,
            "Creches": moradores // 2000,
            "Universidades": moradores // 50000,
            "Bibliotecas": moradores // 15000
        },
        "Saúde": {
            "Hospitais": moradores // 50000,
            "Postos de Saúde": moradores // 10000,
            "Farmácias": moradores // 3000
        },
        "Segurança": {
            "Esquadras de Polícia": moradores // 25000,
            "Bombeiros": moradores // 40000
        },
        "Transporte": {
            "Terminais Rodoviários": moradores // 50000,
            "Empresas de Transporte": moradores // 40000,
            "Pontos de Táxi": moradores // 5000
        },
        "Financeiro": {
            "Bancos": moradores // 10000,
            "Cooperativas de Crédito": moradores // 20000,
            "Caixas Eletrônicos": moradores // 5000
        },
        "Cultura e Lazer": {
            "Centros Culturais": moradores // 20000,
            "Centros de Recreação": moradores // 10000,
            "Quadras Esportivas": moradores // 3000
        },
        "Assistência Social": {
            "CRAS": moradores // 25000,
            "Casas de Acolhimento": moradores // 30000
        },
        "Religião": {
            "Igrejas / Templos": moradores // 1000
        }
    }

# --- Interface Visual ---
st.set_page_config(page_title="Planejador Municipal", layout="centered")
st.title("🏙️ Planejador Municipal - Lubango")

aba = st.sidebar.radio("Navegar para:", ["📋 Planejamento Urbano", "🧑‍🌾 Cadastro de Terrenos", "📑 Lista de Terrenos"])

# --- Aba: Planejamento Urbano ---
if aba == "📋 Planejamento Urbano":
    st.subheader(f"📊 Instituições necessárias para {NOME_MUNICIPIO}")
    st.write(f"População atual: **{POPULACAO_LUBANGO:,} habitantes**")

    servicos = calcular_servicos(POPULACAO_LUBANGO)

    for categoria, itens in servicos.items():
        st.markdown(f"### {categoria}")
        for nome, quantidade in itens.items():
            st.write(f"- {quantidade} {nome}")
        st.markdown("---")

# --- Aba: Cadastro de Terrenos ---
elif aba == "🧑‍🌾 Cadastro de Terrenos":
    st.subheader("📌 Cadastrar um novo terreno")

    with st.form("form_terreno"):
        dono = st.text_input("Nome do dono")
        local = st.text_input("Localização do terreno")
        tamanho = st.number_input("Tamanho (em m²)", min_value=1.0)

        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            novo_terreno = {
                "Dono": dono,
                "Localização": local,
                "Tamanho (m²)": tamanho
            }
            st.session_state.terrenos.append(novo_terreno)
            st.success("✅ Terreno cadastrado com sucesso!")

    # --- Terrenos aleatórios ---
    nomes_ficticios = ["José", "Maria", "António", "Joana", "Carlos", "Ana", "Pedro", "Sofia"]
    locais_ficticios = ["Bairro Popular", "Tchioco", "Arimba", "Munhino", "Mapunda", "Quilemba", "Huila Park"]

    if st.button("🧪 Gerar 5 terrenos aleatórios"):
        for _ in range(5):
            nome = random.choice(nomes_ficticios)
            local = random.choice(locais_ficticios)
            tamanho = round(random.uniform(150.0, 3000.0), 2)

            terreno_aleatorio = {
                "Dono": nome,
                "Localização": local,
                "Tamanho (m²)": tamanho
            }
            st.session_state.terrenos.append(terreno_aleatorio)

        st.success("✅ 5 terrenos aleatórios cadastrados com sucesso!")

# --- Aba: Lista de Terrenos ---
elif aba == "📑 Lista de Terrenos":
    st.subheader("📋 Terrenos cadastrados")

    if not st.session_state.terrenos:
        st.info("Nenhum terreno cadastrado ainda.")
    else:
        for i, terreno in enumerate(st.session_state.terrenos, 1):
            st.markdown(f"**{i}. Dono:** {terreno['Dono']}")
            st.write(f"📍 Local: {terreno['Localização']}")
            st.write(f"📏 Tamanho: {terreno['Tamanho (m²)']} m²")
            st.markdown("---")
