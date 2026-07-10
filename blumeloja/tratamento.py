import pandas as pd
from connection import engine

sql1 = '''
SELECT c."nomeCategoria", SUM(v.quantidade) AS total_vendido FROM vendas v
JOIN produtos p ON v."produtosId" = p.id
JOIN categorias c ON c.id = p."categoriasId"
GROUP BY c."nomeCategoria";
'''

df = pd.read_sql_query(sql1, engine)

total_vendido_categoria = df.groupby('nomeCategoria')['total_vendido'].sum()

sql2 = '''
SELECT vendas."dataHora", vendas.quantidade
FROM vendas;
'''

df = pd.read_sql_query(sql2, engine)

df["dataHora"] = pd.to_datetime(df["dataHora"])
df["hora"] = df["dataHora"].dt.hour

qtde_vendida_hora = df.groupby("hora")["quantidade"].sum()