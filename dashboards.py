import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(layout="wide")
st.title("Dashboard de vendas da Loja do :blue[Candido] :sunglasses:")

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)
col6, col7 = st.columns(2)


df = pd.read_csv("loja.csv", sep=";", decimal=",")
df["Data"] = pd.to_datetime(df["Data"])
df = df.sort_values("Data")

df["Month"] = df["Data"].apply(lambda x: str(x.year) + "-" + str(x.month))
month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]


##############################################################
# 01 Faturamento por loja (diário)
fig_diario = px.bar(df_filtered, x="Data", y="Total",
                  color="Bairro", title="Faturamento diário por loja")

col1.plotly_chart(fig_diario, use_container_width=True)
##############################################################



##############################################################
# 02 Faturamento por tipo de produto
fig_produto = px.bar(df_filtered, x="Data", y="Tipo de produto",
                  color="Bairro", title="Faturamento por tipo de produto",
                  orientation="h")

col2.plotly_chart(fig_produto, use_container_width=True)
##############################################################



##############################################################
# 03 Faturamento por loja (total)
total_bairro = df_filtered.groupby("Bairro")[["Total"]].sum().reset_index()

fig_total = px.bar(total_bairro, x="Bairro", y="Total",
                  title="Faturamento total por loja")

col3.plotly_chart(fig_total, use_container_width=True)
##############################################################



##############################################################
# 04 Formas de pagamento
fig_pagamento = px.pie(df_filtered, values="Total", names="Pagamento",
                  title="Faturamento por tipo de pagamento")

col4.plotly_chart(fig_pagamento, use_container_width=True)
##############################################################



##############################################################
# 05 Média de Avaliações
notas = df_filtered.groupby("Bairro")[["Nota"]].mean().reset_index()

fig_notas = px.bar(notas, y="Nota", x="Bairro",
                    title="Média de Avaliação")
col5.plotly_chart(fig_notas, use_container_width=True)
##############################################################



##############################################################
# 06 Genero
fig_genero = px.pie(df_filtered, values="Total", names="Genero",
                  title="Vendas por gênero")

col6.plotly_chart(fig_genero, use_container_width=True)
##############################################################



##############################################################
# 07 Quantidade de produtos vendidos
df_produtos = df_filtered.groupby("Tipo de produto")[["Quantidade"]].sum()

fig_produto = px.bar(df_produtos, title="Quantidade de produtos vendidos",
                  orientation="v")

col7.plotly_chart(fig_produto, use_container_width=True)
##############################################################