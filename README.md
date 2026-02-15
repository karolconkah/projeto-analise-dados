Este projeto realiza uma análise completa de vendas utilizando:
Python
Pandas
Seaborn / Matplotlib
SQLite (SQL)
Jupyter Notebook
Scikit Learn 
Scipy.stats

O objetivo foi analisar o desempenho de lojas e gerentes, identificar regiões com maior faturamento,, verificar o cumprimento de metas e fazer análises estatísticas em geral. 

Análises realizadas 
Limpeza e tratamento de dados
Criação de novas colunas estratégicas: Cálculo de faturamento, Região
Análise mensal
Ranking de faturamento por loja
Ranking por gerente
Verificação de metas batidas
Agrupamento por região
Mesclagem da tabela gerentes com a tabela de vendas
Visualizações gráficas
Criação e consulta de banco SQL
JOIN entre tabelas no SQLite
Utilização do Scikit Learn para realizar regressão linear simples para a obtenção a análise do valor real em comparação ao valor previsto e para a análise de influencia de variáveis sobre o faturamento
Previsão com Scikit Learn sobre o faturamento mensal dos 3 primeiros próximos meses seguintes da última data mês/ano da tabela do banco de dados 
Utilização do Scipy.stats para testes de hipótese, intervalos de confiança, teste Qui-Quadrado, ANOVA, Levene. 


Principais insights 
Identificação das lojas com maior faturamento.
Comparação mensal entre regiões.
Avaliação do desempenho dos gerentes.
Análise de cumprimento de metas.
Análise das Médias entre os gerentes (por venda e por mês) 
Análise da consistência (variância) entre gerentes.
Análise da média global do faturamento.
Análise sobre proporção de vendas múltiplas.
Análise sobre influência de Produto × Região.

Foi utilizado SQLite para:
Criar tabela de vendas
Criar tabela de gerentes
Realizar JOIN entre tabelas
Criar rankings via SQL

