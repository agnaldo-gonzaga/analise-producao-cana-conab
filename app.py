import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="Cana-de-Açúcar Brasil | CONAB",
    page_icon="🎋",
    layout="wide"
)

st.title("🎋 Análise de Performance e Evolução da Cana-de-Açúcar no Brasil")
st.caption("Dados oficiais da CONAB — Safras 2017/18 a 2025/26")

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cana_limpo.csv", encoding="utf-8")
    return df

@st.cache_data
def load_data_all():
    df_all = pd.read_csv("data/processed/cana_todos_levantamentos.csv", encoding="utf-8")
    df_all["ano_agricola"] = df_all["ano_agricola"].str.strip()
    df_all["uf"] = df_all["uf"].str.strip()
    cols_n = ["area_plantada_mil_ha","producao_mil_t","producao_acucar_mil_t",
              "producao_etanol_total_mil_l","produtcao_atr_kg_t"]
    for c in cols_n:
        df_all[c] = pd.to_numeric(df_all[c], errors="coerce").fillna(0)
    return df_all

try:
    df = load_data()
    df_all = load_data_all()
    data_ok = True
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    data_ok = False

if data_ok:

    # ── Métricas no topo ──────────────────────────────────────────────────────
    prod_total = df["producao_mil_t"].sum()
    safra_record = df.groupby("ano_agricola")["producao_mil_t"].sum().idxmax()
    prod_record = df.groupby("ano_agricola")["producao_mil_t"].sum().max()
    atr_medio = df["produtcao_atr_kg_t"].mean()
    n_estados = df["uf"].nunique()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Produção acumulada", f"{prod_total:,.0f} mil t")
    col2.metric("Safra recorde", safra_record, f"{prod_record:,.0f} mil t")
    col3.metric("ATR médio nacional", f"{atr_medio:.1f} kg/t")
    col4.metric("Estados analisados", n_estados)

    st.divider()

    # ── Sidebar ───────────────────────────────────────────────────────────────
    st.sidebar.header("Filtros")
    regioes = sorted(df["regiao"].dropna().unique().tolist())
    regioes_sel = st.sidebar.multiselect("Região", regioes, default=regioes)
    ufs = sorted(df[df["regiao"].isin(regioes_sel)]["uf"].unique().tolist())
    ufs_sel = st.sidebar.multiselect("Estado (UF)", ufs, default=ufs)
    safras = sorted(df["ano_agricola"].unique().tolist())
    safra_range = st.sidebar.select_slider("Período", options=safras, value=(safras[0], safras[-1]))

    df_f = df[
        df["regiao"].isin(regioes_sel) &
        df["uf"].isin(ufs_sel) &
        df["ano_agricola"].between(safra_range[0], safra_range[1])
    ]

    # ── Tabs ──────────────────────────────────────────────────────────────────
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Produção por Safra",
        "🏆 Top Estados",
        "🍬 Açúcar vs Etanol",
        "🌿 ATR por Estado",
        "🗺️ Evolução Regional",
        "🔍 Precisão dos Levantamentos"
    ])

    # ── Tab 1: Produção por safra ─────────────────────────────────────────────
    with tab1:
        st.subheader("Produção Total de Cana por Safra")
        prod_safra = df_f.groupby("ano_agricola")["producao_mil_t"].sum().reset_index()

        fig1 = px.bar(
            prod_safra, x="ano_agricola", y="producao_mil_t",
            labels={"ano_agricola": "Safra", "producao_mil_t": "Produção (mil t)"},
            color="producao_mil_t", color_continuous_scale="Greens",
            text_auto=".0f"
        )
        fig1.update_layout(showlegend=False, coloraxis_showscale=False,
                           plot_bgcolor="rgba(240,240,240,0.3)")
        st.plotly_chart(fig1, use_container_width=True)

        with st.expander("📌 Insights"):
            st.markdown("""
- **2023/24** registrou o maior volume: **713.214 mil t** (+17% sobre a anterior)
- **2021/22** foi o pior ano, com queda para **585.180 mil t** — geada + seca no Centro-Sul
- Após a queda, o setor demonstrou forte recuperação atingindo novo recorde em 2023/24
- A safra **2025/26** mantém patamar acima da média histórica
""")

    # ── Tab 2: Top 10 estados ─────────────────────────────────────────────────
    with tab2:
        st.subheader("Top Estados — Produção Acumulada")
        n_top = st.slider("Quantos estados exibir?", 5, 20, 10)
        top_n = df_f.groupby("uf")["producao_mil_t"].sum().nlargest(n_top).reset_index()
        top_n_sorted = top_n.sort_values("producao_mil_t")

        fig2 = px.bar(
            top_n_sorted, x="producao_mil_t", y="uf", orientation="h",
            labels={"uf": "Estado", "producao_mil_t": "Produção acumulada (mil t)"},
            color="producao_mil_t", color_continuous_scale="YlGn",
            text=top_n_sorted["producao_mil_t"].apply(lambda x: f"{x:,.1f}".replace(",", ".")),
        )
        fig2.update_traces(textposition="outside", cliponaxis=False)
        fig2.update_layout(
            showlegend=False, coloraxis_showscale=False,
            plot_bgcolor="rgba(240,240,240,0.3)",
            xaxis=dict(showticklabels=False, title=None),
            yaxis=dict(title=None),
            margin=dict(r=130)
        )
        fig2.update_xaxes(range=[0, top_n_sorted["producao_mil_t"].max() * 1.20])
        st.plotly_chart(fig2, use_container_width=True)

        with st.expander("📌 Insights"):
            st.markdown("""
- **SP** concentra ~58% do total acumulado do Top 10
- **GO e MG** formam o segundo bloco com produções similares entre si
- **AL e PE** representam o Nordeste no ranking — presença histórica com menor escala
""")

    # ── Tab 3: Açúcar vs Etanol ───────────────────────────────────────────────
    with tab3:
        st.subheader("Produção de Açúcar e Etanol por Safra")
        ae = df_f.groupby("ano_agricola").agg(
            acucar=("producao_acucar_mil_t", "sum"),
            etanol=("producao_etanol_total_mil_l", "sum")
        ).reset_index()
        ae["etanol_bil_l"] = (ae["etanol"] / 1_000_000).round(2)

        fig3 = make_subplots(specs=[[{"secondary_y": True}]])
        fig3.add_trace(go.Bar(
            x=ae["ano_agricola"], y=ae["acucar"],
            name="Açúcar (mil t)", marker_color="#f4a261",
            text=ae["acucar"].apply(lambda x: f"{x:,.0f}"),
            textposition="outside", cliponaxis=False,
        ), secondary_y=False)
        fig3.add_trace(go.Scatter(
            x=ae["ano_agricola"], y=ae["etanol_bil_l"],
            name="Etanol (bi L)", mode="lines+markers+text",
            line=dict(color="#2196F3", width=2),
            marker=dict(size=7),
            text=ae["etanol_bil_l"].apply(lambda x: f"{x:.2f}"),
            textposition="top center",
        ), secondary_y=True)
        fig3.update_layout(
            plot_bgcolor="rgba(240,240,240,0.3)",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )
        fig3.update_yaxes(title_text="Açúcar (mil t)", secondary_y=False,
                          range=[0, ae["acucar"].max() * 1.25])
        fig3.update_yaxes(title_text="Etanol (bilhões L)", secondary_y=True,
                          range=[ae["etanol_bil_l"].min() * 0.90, ae["etanol_bil_l"].max() * 1.15],
                          showgrid=False)
        st.plotly_chart(fig3, use_container_width=True)

        with st.expander("📌 Insights"):
            st.markdown("""
- **2023/24**: pico histórico de açúcar com **45.678,8 mil t**
- **2019/20**: máxima de etanol com **34 bilhões de litros**
- **2021/22**: pior safra para ambos os derivados — impacto climático duplo
- A flexibilidade das usinas (flex) absorve choques sem grandes desvios estruturais
""")

    # ── Tab 4: ATR ────────────────────────────────────────────────────────────
    with tab4:
        st.subheader("ATR Médio por Estado e por Safra")

        col_a, col_b = st.columns(2)

        with col_a:
            atr_safra = df_f.groupby("ano_agricola")["produtcao_atr_kg_t"].mean().reset_index()
            fig4a = px.line(
                atr_safra, x="ano_agricola", y="produtcao_atr_kg_t",
                markers=True,
                labels={"ano_agricola": "Safra", "produtcao_atr_kg_t": "ATR médio (kg/t)"},
                title="Evolução do ATR Médio por Safra"
            )
            fig4a.update_traces(line_color="#1D9E75")
            st.plotly_chart(fig4a, use_container_width=True)

        with col_b:
            atr_estado = df_f.groupby("uf")["produtcao_atr_kg_t"].mean().reset_index()
            atr_estado.columns = ["uf", "atr_medio"]
            atr_top = atr_estado.sort_values("atr_medio", ascending=False).head(15)

            fig4b = px.bar(
                atr_top.sort_values("atr_medio"),
                x="atr_medio", y="uf", orientation="h",
                labels={"uf": "Estado", "atr_medio": "ATR médio (kg/t)"},
                color="atr_medio", color_continuous_scale="YlGn",
                title="Top 15 Estados por ATR Médio"
            )
            fig4b.update_layout(coloraxis_showscale=False,
                                xaxis=dict(range=[atr_top["atr_medio"].min() * 0.97,
                                                  atr_top["atr_medio"].max() * 1.03]))
            st.plotly_chart(fig4b, use_container_width=True)

        with st.expander("📌 Insights"):
            st.markdown("""
- **MT** lidera com **140,09 kg/t** — condições edafoclimáticas favoráveis
- **GO e MG** formam o segundo bloco de alta performance
- **Nordeste** (AL, PE) apresenta os menores índices (~128 kg/t) — diferença de ~12 kg/t frente ao MT
- ATR tem baixa correlação com volume: estados menores podem ser tão eficientes quanto os grandes
""")

    # ── Tab 5: Evolução regional ──────────────────────────────────────────────
    with tab5:
        st.subheader("Evolução da Produção por Região")
        prod_reg = df_f.groupby(["ano_agricola", "regiao"])["producao_mil_t"].sum().reset_index()

        fig5 = px.line(
            prod_reg, x="ano_agricola", y="producao_mil_t",
            color="regiao", markers=True,
            labels={"ano_agricola": "Safra", "producao_mil_t": "Produção (mil t)", "regiao": "Região"},
        )
        fig5.update_layout(plot_bgcolor="rgba(240,240,240,0.3)")
        st.plotly_chart(fig5, use_container_width=True)

        # tabela resumo
        resumo = df_f.groupby("regiao")["producao_mil_t"].agg(
            total="sum", media="mean", maximo="max", minimo="min"
        ).round(1).sort_values("total", ascending=False)
        resumo.columns = ["Total (mil t)", "Média (mil t)", "Máximo (mil t)", "Mínimo (mil t)"]
        st.dataframe(resumo, use_container_width=True)

        with st.expander("📌 Insights"):
            st.markdown("""
- **Sudeste** domina com ~60% do total em todos os anos
- **Centro-Oeste** apresentou crescimento mais consistente e estável
- **Nordeste** registrou o maior crescimento relativo do período: +34%
- **Sul** é a única região com contração líquida (-3,5%)
""")

    # ── Tab 6: Precisão dos levantamentos ─────────────────────────────────────
    with tab6:
        st.subheader("Variação entre 1º Levantamento e Resultado Final")

        lev1 = df_all[df_all["id_levantamento"] == 1][["ano_agricola", "uf", "producao_mil_t"]]\
               .rename(columns={"producao_mil_t": "p1"})
        levF = df_all[df_all["id_levantamento"] == 99][["ano_agricola", "uf", "producao_mil_t"]]\
               .rename(columns={"producao_mil_t": "pF"})
        comp = pd.merge(lev1, levF, on=["ano_agricola", "uf"])
        comp = comp[(comp["pF"] > 0) & (comp["p1"] > 0)]
        comp["erro_pct"] = ((comp["pF"] - comp["p1"]) / comp["pF"] * 100).abs()

        if not comp.empty:
            fig6 = px.box(
                comp, x="uf", y="erro_pct",
                labels={"uf": "Estado", "erro_pct": "Variação absoluta (%)"},
                color="uf"
            )
            fig6.update_layout(showlegend=False, plot_bgcolor="rgba(240,240,240,0.3)")
            st.plotly_chart(fig6, use_container_width=True)
        else:
            st.info("Dados de levantamento 99 não encontrados. Verifique o id_levantamento no arquivo cana_todos_levantamentos.csv")

        with st.expander("📌 Insights"):
            st.markdown("""
- **RJ** é o outlier crítico com mediana próxima a 55% de variação
- **SP, SE, PI e TO** são os estados mais confiáveis para projeções iniciais
- A maioria dos estados opera no intervalo de 10–20% de variação — padrão esperado
""")