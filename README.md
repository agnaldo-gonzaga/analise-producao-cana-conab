# 🎋 Análise de Performance e Evolução da Cana-de-Açúcar no Brasil

> Dados oficiais da CONAB — Companhia Nacional de Abastecimento | Safras 2017/18 a 2025/26

---

## 📌 Sobre o Projeto

Pipeline completo de dados (ETL → EDA → Visualizações) sobre a produção nacional de 
cana-de-açúcar, transformando dados governamentais brutos em indicadores de 
produtividade por estado e região.

---

## 🚀 Perguntas Respondidas

- Qual a evolução do TCH (Toneladas de Cana por Hectare) nas últimas safras?
- Quais estados lideram em produtividade vs. área plantada?
- Como evoluiu a produção de açúcar vs. etanol ao longo das safras?
- Quais as variações sazonais entre as regiões Centro-Sul e Norte-Nordeste?

---

## 💡 Principais Achados

- **SP** concentra ~58% da produção acumulada do Top 10 estados
- **2023/24** foi a safra recorde, com 713.214 mil t (+17% sobre a anterior)
- **2021/22** foi o pior ano da série, impactado por geada + seca
- Setor demonstrou forte resiliência, retomando crescimento no ciclo seguinte

---

## 📊 Visualizações

### Produção Total por Safra
![Produção por Safra](reports/figures/01_producao_por_safra.png)

### 📌 Insights — Produção Total por Safra

- **2023/24** registrou o **maior volume** do período: **713.214 mil t**, um crescimento de ~17% sobre a safra anterior
- **2021/22** foi o **pior ano** da série, com queda para **585.180 mil t** — reflexo de adversidades climáticas (geada + seca)
- Após a queda em 2021/22, o setor demonstrou **forte recuperação**, atingindo novo recorde em 2023/24
- A safra **2025/26** apresenta leve recuo em relação ao pico, mas mantém patamar **acima da média histórica**

> 💡 **Tendência geral:** crescimento consistente ao longo do período, com resiliência do setor mesmo após choques climáticos.

---

### Top 10 Estados Produtores
![Top 10 Estados](reports/figures/02_top10_estados.png)

### 📌 Insights — Produção Acumulada por Estado (UF)

- **SP** registrou a **maior produção acumulada** do ranking: **3.062.627,8 mil t**, representando sozinho mais de **58% do total** do Top 10
- **GO e MG** formam o **segundo bloco**, com 668.476,6 e 649.145,9 mil t respectivamente — produções similares entre si, porém **4,6x menores** que SP
- **MS e PR** ocupam a **faixa intermediária**, com 434.190,5 e 312.850,2 mil t — estados em expansão no Centro-Sul com crescente participação nacional
- **AL e PE** representam o **Nordeste** no ranking, com 159.828,2 e 115.789,3 mil t — presença histórica, mas com escala menor frente ao eixo Centro-Sul
- **MT, PB, BA e RN** fecham o Top 10 com produções abaixo de **153 mil t**, sinalizando participação ainda **incipiente no acumulado**

> 💡 **Tendência geral:** produção nacional fortemente concentrada no Centro-Sul, com SP como protagonista isolado — padrão que reflete décadas de expansão agroindustrial no estado.

---

### Açúcar vs Etanol por safra
![Açúcar vs Etanol por safra](reports/figures/03_acucar_vs_etanol.png)

### 📌 Insights - Açúcar vs Etanol por safra

- **2023/24** registrou o **pico histórico de açúcar**: **45.678,8 mil t** — maior volume das 8 safras, superando em +10,7% o segundo colocado (2024/25, 44.853,6 mil t), sinalizando dois anos consecutivos de recorde no segmento sólido
- **2019/20** concentrou a **máxima de etanol**: **34,00 bilhões de litros** — após a quebra de 2017/18 (27,24 bi L), o setor acelerou a conversão de cana para líquido, atingindo o topo do período analisado
- **2021/22 foi o piso duplo**: menor produção de açúcar (35.049,1 mil t) e de etanol (26,78 bi L) no ciclo — reflexo de adversidades climáticas e queda na disponibilidade de cana na região Centro-Sul
- A **proporção de cana para etanol oscilou entre 26,78% e 34,00%**, com média de ~29,8% — variação relativamente estreita, indicando que a flexibilidade produtiva das usinas (flex) absorve choques sem grandes desvios estruturais
- **Trajetória pós-2021/22**: ambos os indicadores se recuperam em conjunto, mas com dinâmicas distintas — açúcar em alta consistente (+30,3%), etanol em recuperação moderada (+9,6%), sugerindo **viés crescente de alocação para o sólido** nas safras recentes

> 💡 **Tendência geral:** o setor sucroenergético demonstra resiliência cíclica, com picos alternados entre açúcar e etanol conforme incentivos de preço — mas a aceleração pós-2022/23 no açúcar aponta para uma janela de rentabilidade que tem puxado a alocação produtiva para esse lado da balança.

---


## 🛠️ Tecnologias

| Categoria | Ferramentas |
|---|---|
| Linguagem | Python 3.x |
| Manipulação | Pandas, NumPy |
| Visualização | Matplotlib, Seaborn, Plotly |

---

## 📁 Estrutura do Repositório

```
ANALISE-PRODUCAO-CANA-CONAB/
├── data/
│   ├── raw/                  ← dados originais da CONAB
│   └── processed/            ← dados limpos e prontos para análise
├── notebooks/
│   ├── 01_limpeza_dados.ipynb
│   ├── 02_analise_exploratoria.ipynb
│   └── 03_visualizacoes.ipynb
├── reports/
│   └── figures/              ← gráficos exportados
├── requirements.txt
└── README.md
```

---

## ▶️ Como Executar

```bash
# Clone o repositório
git clone https://github.com/agnaldo-gonzaga/analise-producao-cana-conab.git

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute os notebooks na ordem
# 01 → 02 → 03
```

---

## 🤝 Contato

- LinkedIn: [agnaldo-gonzaga](https://www.linkedin.com/in/agnaldo-gonzaga/)

---

*Projeto desenvolvido como parte da jornada em Data Science e Analytics.*