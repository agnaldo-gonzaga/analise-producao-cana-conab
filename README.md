# 🎋 Análise de Performance e Evolução da Cana-de-Açúcar

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

## 📊 Visualizações

### Produção Total por Safra
![Produção por Safra](reports/figures/01_producao_por_safra.png)

---

## 🛠️ Tecnologias

| Categoria | Ferramentas |
|---|---|
| Linguagem | Python 3.x |
| Manipulação | Pandas, NumPy |
| Visualização | Matplotlib, Seaborn, Plotly |

---

## 📁 Estrutura do Repositório

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