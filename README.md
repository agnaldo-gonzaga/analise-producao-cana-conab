# 🎋 Análise de Performance: Produção de Cana-de-Açúcar (Dados CONAB)

Este projeto realiza o pipeline completo de dados (ETL e EDA) sobre a produção nacional de cana-de-açúcar, utilizando dados oficiais da **CONAB**. O foco é transformar dados governamentais brutos em indicadores de produtividade por estado e região.

---

## 🚀 Objetivo do Projeto
Demonstrar habilidades em engenharia de dados (limpeza e estruturação) e análise exploratória para responder perguntas estratégicas do setor agrícola:
* Qual a evolução do **TCH (Toneladas de Cana por Hectare)** nas últimas safras?
* Quais estados lideram em produtividade vs. área plantada?
* Identificação de variações sazonais na produção das regiões Centro-Sul e Norte-Nordeste.

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python 3.x
* **Manipulação de Dados:** Pandas, NumPy
* **Visualização:** Matplotlib, Seaborn

## 📁 Estrutura do Repositório
* `01_limpeza_dados.ipynb`: Notebook com todo o processo de tratamento, tratamento de nulos e normalização das unidades de medida.
* `cana_todos_levantamentos.csv`: Dataset contendo o histórico consolidado de safras.

## 📊 Processo de ETL (Extração, Transformação e Carga)
Nesta fase inicial (contida no script de limpeza), realizei:
1. **Padronização:** Conversão de tipos de dados para otimização de memória.
2. **Tratamento de Strings:** Limpeza de nomes de estados e categorias de produtos.
3. **Cálculos de Negócio:** Criação de colunas para cálculo de rendimento médio.

---



## 🤝 Contato
- **LinkedIn:** [https://www.linkedin.com/in/agnaldo-gonzaga/]


---
*Projeto desenvolvido como parte da jornada em Data Science e Analytics.*
