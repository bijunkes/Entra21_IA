import pandas as pd
from connection import engine
import streamlit as st
import tratamento as tr
import datetime

# sql = '''
# SELECT vendas."dataHora", vendas."quantidade", produtos."nomeProduto", categorias."nomeCategoria" FROM vendas
# INNER JOIN produtos ON produtos.id = vendas."produtosId"
# INNER JOIN categorias ON categorias.id = produtos."categoriasId";
# '''

# df = pd.read_sql(sql, engine)

# st.set_page_config(layout="wide")

# col1, col2 = st.columns(2)

# with col1: 
    
#     st.text("Quantidade de produtos vendidos por categoria")
    
#     with st.container(border=True):

#         st.bar_chart(tr.total_vendido_categoria, horizontal=False)
        
# with col2: 
    
#     st.text("Quantidade de produtos vendidos por hora")
    
#     with st.container(border=True):

#         st.line_chart(tr.qtde_vendida_hora)
    
# df = pd.DataFrame(
#     {
#         'nomeCategoria': ['Meias', 'Cuecas', 'Cintos']
#     }
# )

# df.to_sql(
#     name='categorias',
#     con=engine,
#     if_exists='append',
#     index=False
# )

# df = pd.DataFrame(
#     {
#         'nomeProduto': [
#             'Meia Esportiva',
#             'Cueca Boxer Algodão',
#             'Cinto de Couro'
#         ],
#         'codigoBarras': [
#             '1234567890',
#             '9876543210',
#             '4567891230'
#         ],
#         'categoriasId': [
#             4,
#             5,
#             6
#         ]
#     }
# )

# df.to_sql(
#     name='produtos',
#     con=engine,
#     if_exists='append',
#     index=False
# )

# df = pd.DataFrame(
#     {
#         'dataHora': [
#             datetime.datetime.now(),
#             datetime.datetime.now(),
#             datetime.datetime.now()
#         ],
#         'quantidade': [
#             6,
#             3,
#             2
#         ],
#         'produtosId': [
#             8,
#             9,
#             10
#         ]
#     }
# )

# df.to_sql(
#     name='vendas',
#     con=engine,
#     if_exists='append',
#     index=False
# )
