Análise de Vendas com Python e Estatística

Sobre o projeto

Este projeto realiza uma análise completa de vendas com foco em desempenho de lojas, gerentes e regiões, utilizando técnicas de análise exploratória de dados, estatística inferencial e modelagem preditiva.

O objetivo foi identificar padrões de faturamento, avaliar o cumprimento de metas e gerar previsões futuras com base nos dados históricos.

Tecnologias utilizadas

Python

Pandas

Seaborn

Matplotlib

SQLite

Jupyter Notebook

Scikit-Learn

SciPy (scipy.stats)

Etapas do projeto
1. Limpeza e tratamento de dados

Remoção de inconsistências

Tratamento de valores ausentes

Criação de colunas estratégicas (ex: Região)

2. Análise exploratória

Análise mensal de faturamento

Ranking de faturamento por loja

Ranking de desempenho por gerente

Verificação de metas batidas

Agrupamento por região

Mesclagem da tabela de gerentes com vendas

3. Visualizações

Gráficos comparativos por região

Evolução mensal do faturamento

Comparações entre gerentes

Distribuições e variância

4. Banco de dados

Utilização de SQLite para:

Criação da tabela de vendas

Criação da tabela de gerentes

JOIN entre tabelas

Criação de rankings via SQL

5. Modelagem preditiva

Regressão linear simples com Scikit-Learn

Comparação entre valores reais e previstos

Análise de influência de variáveis

Previsão de faturamento para os 3 meses seguintes

6. Estatística inferencial

Utilização do scipy.stats para:

Testes de hipóteses

Intervalos de confiança

Teste Qui-Quadrado

ANOVA

Teste de Levene (análise de variância)

Principais insights obtidos

Identificação das lojas com maior faturamento

Comparação de desempenho entre regiões

Avaliação do desempenho individual dos gerentes

Análise de cumprimento de metas

Comparação de médias entre gerentes

Análise de consistência (variância)

Proporção de vendas múltiplas

Influência Produto × Região no faturamento

Objetivo

Aplicar técnicas de análise de dados, estatística e machine learning para gerar insights estratégicos e previsões de desempenho.


Dashboard Interativo de Análise de Vendas

Aplicação desenvolvida em Python utilizando Streamlit para análise dinâmica de desempenho de vendas por gerente.

Acesse o dashboard online:
https://dashboard-vendas-karoline.streamlit.app

Tecnologias Utilizadas

Python 3

Pandas

Plotly

Streamlit

Git e GitHub

Funcionalidades

O dashboard permite:

Filtro por gerente

Filtro por período (Mês/Ano)

Métricas dinâmicas:

Faturamento total

Média de faturamento

Total de registros

Evolução mensal do faturamento

Comparação mensal entre gerentes

Ranking automático de performance

Crescimento percentual mês a mês

Índice de consistência (Coeficiente de Variação)

Objetivo do Projeto

Demonstrar aplicação prática de análise de dados utilizando:

Agregações com Pandas

Cálculo de métricas estatísticas

Visualização interativa com Plotly

Deploy em produção via Streamlit Cloud

O projeto simula um cenário real de análise de performance comercial, permitindo identificar:

Top performers

Estabilidade de desempenho

Tendências mensais

Variações sazonais

Principais Análises Estatísticas Implementadas

Média e desvio padrão

Crescimento percentual mensal

Ranking por faturamento

Coeficiente de variação (CV%)

Análise de consistência de performance

Como Executar Localmente

Clone o repositório:

git clone https://github.com/karolconkah/projeto-analise-dados

Instale as dependências:

pip install -r requirements.txt

Execute a aplicação:

streamlit run dashboard.py

Deploy

Aplicação hospedada via Streamlit Community Cloud.

Autora

Karoline Vieira Neves
Estudante de Ciência de Dados
Foco em análise de dados, estatística aplicada e visualização interativa.
