
import streamlit as st
import pandas as pd
import random

# Título
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏙️ Planejador Municipal - Lubango</h1>", unsafe_allow_html=True)
st.markdown("---")

# Dados iniciais
habitantes = 776_249
st.markdown(f"### 👥 População total: `{habitantes}` habitantes")

# Estimativa de serviços públicos
def estimar_servicos(habitantes):
    return {
        "Hospitais": max(1, habitantes // 100_000),
        "Escolas": max(1, habitantes // 10_000),
        "Bibliotecas": max(1, habitantes // 50_000),
        "Esquadras de Polícia": max(1, habitantes // 50_000),
        "Bancos": max(1, habitantes // 25_000),
        "Centros de Recreação": max(1, habitantes // 20_000),
        "Empresas de Transporte": max(1, habitantes // 100_000),
    }

servicos = estimar_servicos(habitantes)

with st.expander("📊 Ver estimativa de instituições necessárias"):
    for nome, quantidade in servicos.items():
        st.markdown(f"- **{nome}**: {quantidade}")

# Banco de dados de terrenos
st.markdown("---")
st.markdown("## 🧾 Cadastro de Terrenos")

if "terrenos" not in st.session_state:
    st.session_state.terrenos = []

col1, col2 = st.columns(2)
with col1:
    nome_dono = st.text_input("Nome do dono")
with col2:
    medida = st.text_input("Medida do terreno (ex: 30x20 m²)")

if st.button("💾 Cadastrar Terreno"):
    if nome_dono and medida:
        st.session_state.terrenos.append({"Dono": nome_dono, "Medida": medida})
        st.success("Terreno cadastrado com sucesso!")
    else:
        st.warning("Por favor, preencha todos os campos.")

if st.button("✨ Gerar 5 terrenos aleatórios"):
    nomes_exemplo = ["Ana", "Carlos", "Marta", "João", "Pedro", "Luciana", "Fernando"]
    for _ in range(5):
        nome = random.choice(nomes_exemplo)
        largura = random.randint(10, 100)
        comprimento = random.randint(10, 100)
        st.session_state.terrenos.append({
            "Dono": nome,
            "Medida": f"{largura}x{comprimento} m²"
        })
    st.success("5 terrenos aleatórios foram gerados!")

# Mostrar tabela de terrenos cadastrados
st.markdown("### 📋 Terrenos cadastrados")
df = pd.DataFrame(st.session_state.terrenos)
st.dataframe(df, use_container_width=True)

# Exportar dados
if not df.empty:
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("📥 Baixar como CSV", data=csv, file_name="terrenos_lubango.csv", mime="text/csv")
