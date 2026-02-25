import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

st.title("📊 Dashboard de Vendas")


@st.cache_data
def load_data():
    return pd.read_csv("df_final_dashboard.csv")

df = load_data()

st.success("Dados carregados com sucesso!")


gerentes = df["Gerente"].unique()
gerente_selecionado = st.sidebar.selectbox("Selecione o Gerente", ["Todos"] + list(gerentes))

if gerente_selecionado != "Todos":
    df = df[df["Gerente"] == gerente_selecionado]


st.subheader("Métricas Gerais")

col1, col2, col3 = st.columns(3)

col1.metric("Faturamento Total", f"R$ {df['Faturamento'].sum():,.2f}")
col2.metric("Média de Faturamento", f"R$ {df['Faturamento'].mean():,.2f}")
col3.metric("Total de Registros", len(df))


st.subheader("Faturamento por Gerente")

faturamento_gerente = df.groupby("Gerente")["Faturamento"].sum().reset_index()

fig = px.bar(
    faturamento_gerente,
    x="Gerente",
    y="Faturamento",
    color="Gerente",
    title="Total de Faturamento por Gerente"
)

st.plotly_chart(fig, use_container_width=True)


# -------- EVOLUÇÃO MENSAL --------
st.subheader("Evolução Mensal do Faturamento")


if "Mes_Ano" not in df.columns:
    if "Data" in df.columns:
        df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
        df["Mes_Ano"] = df["Data"].dt.to_period("M").astype(str)
    else:
        st.warning("Não encontrei 'Mes_Ano' nem 'Data' para montar a evolução mensal.")
        st.stop()


meses = sorted(df["Mes_Ano"].dropna().unique().tolist())
mes_selecionado = st.sidebar.multiselect("Mês/Ano", options=meses, default=meses)

df_mes = df[df["Mes_Ano"].isin(mes_selecionado)].copy()


fat_mes = (
    df_mes.groupby("Mes_Ano")["Faturamento"]
    .sum()
    .reset_index()
    .sort_values("Mes_Ano")
)

fig_mes = px.line(
    fat_mes,
    x="Mes_Ano",
    y="Faturamento",
    markers=True,
    title="Faturamento total por mês"
)

st.plotly_chart(fig_mes, use_container_width=True)


# -------- COMPARAÇÃO ENTRE GERENTES --------
st.subheader("Comparação de Faturamento por Gerente (Evolução Mensal)")

df_comp = df.copy()


if "Mes_Ano" not in df_comp.columns:
    if "Data" in df_comp.columns:
        df_comp["Data"] = pd.to_datetime(df_comp["Data"], errors="coerce")
        df_comp["Mes_Ano"] = df_comp["Data"].dt.to_period("M").astype(str)


fat_comp = (
    df_comp.groupby(["Mes_Ano", "Gerente"])["Faturamento"]
    .sum()
    .reset_index()
    .sort_values("Mes_Ano")
)

fig_comp = px.line(
    fat_comp,
    x="Mes_Ano",
    y="Faturamento",
    color="Gerente",
    markers=True,
    title="Evolução Mensal por Gerente"
)

st.plotly_chart(fig_comp, use_container_width=True)

# -------- RANKING DE GERENTES --------
st.subheader("🏆 Ranking de Gerentes (Período Selecionado)")

ranking = (
    df_mes.groupby("Gerente")["Faturamento"]
    .sum()
    .reset_index()
    .sort_values("Faturamento", ascending=False)
)

ranking["Posição"] = range(1, len(ranking) + 1)

st.dataframe(ranking, use_container_width=True)

# Destaque Top 3
if len(ranking) >= 1:
    st.success(f"🥇 1º Lugar: {ranking.iloc[0]['Gerente']} - R$ {ranking.iloc[0]['Faturamento']:,.2f}")

if len(ranking) >= 2:
    st.info(f"🥈 2º Lugar: {ranking.iloc[1]['Gerente']} - R$ {ranking.iloc[1]['Faturamento']:,.2f}")

if len(ranking) >= 3:
    st.warning(f"🥉 3º Lugar: {ranking.iloc[2]['Gerente']} - R$ {ranking.iloc[2]['Faturamento']:,.2f}")


    # -------- CRESCIMENTO PERCENTUAL MÊS A MÊS --------
st.subheader("📈 Crescimento Percentual Mensal por Gerente")

df_growth = df_mes.copy()


fat_growth = (
    df_growth.groupby(["Mes_Ano", "Gerente"])["Faturamento"]
    .sum()
    .reset_index()
    .sort_values(["Gerente", "Mes_Ano"])
)


fat_growth["Crescimento_%"] = (
    fat_growth.groupby("Gerente")["Faturamento"]
    .pct_change() * 100
)

fig_growth = px.line(
    fat_growth,
    x="Mes_Ano",
    y="Crescimento_%",
    color="Gerente",
    markers=True,
    title="Crescimento Percentual Mês a Mês"
)

st.plotly_chart(fig_growth, use_container_width=True)


# -------- ÍNDICE DE CONSISTÊNCIA (DESVIO PADRÃO MENSAL) --------
st.subheader("🎯 Índice de Consistência (Desvio padrão do faturamento mensal)")

def br_money(x):
    try:
        return f"R$ {float(x):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "R$ 0,00"


mensal_gerente = (
    df_mes.groupby(["Mes_Ano", "Gerente"])["Faturamento"]
    .sum()
    .reset_index()
)


consistencia = (
    mensal_gerente.groupby("Gerente")["Faturamento"]
    .agg(
        Media_Mensal="mean",
        Desvio_Padrao_Mensal="std",
        Min_Mensal="min",
        Max_Mensal="max",
        Meses="count"
    )
    .reset_index()
)


consistencia["CV_%"] = (consistencia["Desvio_Padrao_Mensal"] / consistencia["Media_Mensal"]) * 100


consistencia["Desvio_Padrao_Mensal"] = consistencia["Desvio_Padrao_Mensal"].fillna(0)
consistencia["CV_%"] = consistencia["CV_%"].fillna(0)


q1 = consistencia["CV_%"].quantile(0.33)
q2 = consistencia["CV_%"].quantile(0.66)

def semaforo(cv):
    if cv <= q1:
        return "🟢 Alta consistência"
    elif cv <= q2:
        return "🟡 Consistência média"
    return "🔴 Baixa consistência"

consistencia["Consistência"] = consistencia["CV_%"].apply(semaforo)


consistencia = consistencia.sort_values(["CV_%", "Desvio_Padrao_Mensal"], ascending=True)


consistencia_fmt = consistencia.copy()
consistencia_fmt["Media_Mensal"] = consistencia_fmt["Media_Mensal"].map(br_money)
consistencia_fmt["Desvio_Padrao_Mensal"] = consistencia_fmt["Desvio_Padrao_Mensal"].map(br_money)
consistencia_fmt["Min_Mensal"] = consistencia_fmt["Min_Mensal"].map(br_money)
consistencia_fmt["Max_Mensal"] = consistencia_fmt["Max_Mensal"].map(br_money)
consistencia_fmt["CV_%"] = consistencia_fmt["CV_%"].map(lambda v: f"{v:.2f}%")

st.dataframe(
    consistencia_fmt[["Gerente", "Consistência", "CV_%", "Media_Mensal", "Desvio_Padrao_Mensal", "Min_Mensal", "Max_Mensal", "Meses"]],
    use_container_width=True
)

# Gráfico do CV% (usar o numérico original)
fig_cons = px.bar(
    consistencia,
    x="Gerente",
    y="CV_%",
    color="Consistência",
    title="Coeficiente de Variação (CV%) — menor = mais consistente"
)
st.plotly_chart(fig_cons, use_container_width=True)

# Destaque automático
top = consistencia.iloc[0]
st.success(
    f"✅ Mais consistente no período: **{top['Gerente']}** "
    f"(CV: {top['CV_%']:.2f}%, desvio padrão mensal: {br_money(top['Desvio_Padrao_Mensal'])})"
)


st.caption("CV% = (desvio padrão mensal / média mensal) × 100. Menor CV% indica maior estabilidade.")