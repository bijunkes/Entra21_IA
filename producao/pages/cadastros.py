import streamlit as st
from sqlalchemy import create_engine
import pandas as pd

USUARIO = 'root'
SENHA = 'admin'
HOST = 'localhost'
PORTA = 3306
NOME_BANCO = 'producao'

url_conexao = f'mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORTA}/{NOME_BANCO}'
engine = create_engine(url_conexao)


st.set_page_config(page_title='Cadastro de Produção', page_icon='📊', layout='wide')
st.title('Cadastro de Produção')

with st.form('cadastro_producao', clear_on_submit=True):
    col1, col2 = st.columns([0.3, 0.7])
    
    with col1:
        data_producao = st.date_input('Data Produção')
        produto = st.text_input('Produto')
        lote = st.text_input('Lote') 
        
    with col2:
        col1_1, col2_2 = st.columns(2)
        
        with col1_1:
            turno = st.radio('Unidade de Medida', ['Manhã', 'Tarde', 'Noite'], horizontal=True)
            
        with col2_2:
            unidade_medida = st.radio('Unidade de Medida', ['UN', 'L'], horizontal=True)
            
        operador = st.text_input('Operador')
        quantidade_produzida = st.number_input('Quantidade Produzida', min_value=1)

    observacoes = st.text_input('Observações')
    
    enviar = st.form_submit_button("Cadastrar", use_container_width=True, type='primary')
    if enviar:
        try:
            dados = {
                'data_producao': data_producao,
                'produto': produto,
                'lote': lote,
                'quantidade_produzida': quantidade_produzida,
                'unidade': unidade_medida,
                'operador': operador,
                'turno': turno,
                'observacoes': ''
            }
            
            df_cadastro = pd.DataFrame([dados])
            
            df_cadastro.to_sql(
                name='producao',
                con=engine,
                if_exists='append',
                index=False
            )
            st.success('Produto Cadastrado', icon="✅")
        except Exception as e:
            st.error(f'This is an error {e}', icon="🚨")