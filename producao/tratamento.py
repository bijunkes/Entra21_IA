import pandas as pd
from connection import conn

# Carregar dados
sql = 'select * from producao'
df = pd.read_sql_query(sql, conn)

# Criar colunas adicionais
df['variacao_producao'] = df['quantidade_produzida'].diff()
df['perc_variacao'] = df['quantidade_produzida'].pct_change()*100

# Totalizadores
total_produzido = df['quantidade_produzida'].sum()
media_producao = df['quantidade_produzida'].mean()

# Novos dfs
producao_ultimos_dias = df.iloc[-1]
producao_turnos = df.groupby('turno')['quantidade_produzida'].sum()