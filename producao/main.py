import streamlit as st
import tratamento as tr

st.set_page_config(page_title='Acompanhamento de Produção', page_icon='📊')
st.title('Acompanhamento de Produção')

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric('Producao Total', tr.total_produzido)

with col2:
    st.metric("Producao Media", tr.media_producao)

with col3:
    st.metric("Dia Anterior", tr.producao_ultimos_dias['quantidade_produzida'], delta=tr.producao_ultimos_dias['perc_variacao'])

with col4:
    st.bar_chart(tr.producao_turnos, horizontal=True)

st.line_chart(tr.df, x='data_producao', y='quantidade_produzida')