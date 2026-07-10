import streamlit as st
import pandas as pd
from sqlalchemy import text
from prompt import gerar_sql, limpar_sql, validar_sql, gerar_grafico
from connection import engine
import plotly.express as px
import json

def executar_sql(sql):
    with engine.connect() as conn:
        df = pd.read_sql(text(sql), conn)
    return df

if 'sql_gerado' not in st.session_state:
    st.session_state.sql_gerado = ''
    
st.set_page_config(layout='wide')

col1, col2 = st.columns([0.4, 0.6])

with col1:
    
    pergunta = st.text_area('Qual sua pergunta?', height=120, placeholder='Total de produtos vendido em Julho de 2026')
    
    if st.button('Gerar SQL'):
        
        if not pergunta:
            st.warning('Descreva qual sua pergunta')
            
        else:
            with st.spinner('Gerando SQL com Groq...'):
                sql = gerar_sql(pergunta)
                valido, mensagem = validar_sql(sql)
                
                if valido:
                    st.session_state.sql_gerado = sql
                    st.success('SQL gerado com sucesso')
                    st.code(sql, language="sql")
                    
with col2:
    
    sql_editavel = st.text_area('SQL para execução', value=st.session_state.sql_gerado, height=200)
    
    if st.button('Executar Consulta'):
        valido, mensagem, = validar_sql(sql_editavel)
        
        if not valido:
            st.error(mensagem)
        else:
            try:
                with st.spinner('Executando consulta...'):
                    df = executar_sql(sql_editavel)
                st.success('Consulta executada')
                
                st.dataframe(df, use_container_width=True)
                st.session_state.df_resultado = df
                
            except Exception as e:
                st.error('Erro ao executar SQL')
                st.exception(e)
                
if "df_resultado" in st.session_state:

    st.divider()

    st.subheader("Configuração do gráfico")

    especificacoes = st.text_area(
        "Como deseja o gráfico?",
        placeholder="""Exemplo:
Gráfico de área rosa.
Título: Crescimento das vendas.
Mostrar valores.
"""
    )


    if st.button("Gerar Gráfico"):

        with st.spinner("Gerando gráfico..."):

            configuracao = gerar_grafico(
                st.session_state.df_resultado,
                especificacoes
            )

        df = st.session_state.df_resultado

        tipo = configuracao["tipo"]
        cor = configuracao["cor"]
        titulo = configuracao["titulo"]
        
        if tipo == "bar":

            fig = px.bar(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title=titulo,
                color_discrete_sequence=[cor]
            )

        elif tipo == "line":

            fig = px.line(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title=titulo,
                color_discrete_sequence=[cor]
            )

        elif tipo == "area":

            fig = px.area(
                df,
                x=df.columns[0],
                y=df.columns[1],
                title=titulo,
                color_discrete_sequence=[cor]
            )

        st.plotly_chart(
            fig,
            use_container_width=True
        )