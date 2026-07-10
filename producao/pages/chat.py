import os
import streamlit as st
from groq import Groq
from tratamento import df
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY")
)

st.set_page_config(page_title='Chat com DataFrame', page_icon='📊')
st.title('📊 Chatbot com DataFrame')

MAX_ROWS = 100
contexto_df = df.head(MAX_ROWS).to_markdown(index=False)

system_prompt = f"""
Atue como um assistente especializado em analizar tabelas.

A tabela disponível é:

{contexto_df}

Responda apenas com as informações da tabela.

Não alucine para responder perguntas que não possuem informações disponíveis para respodê-las, somente avise que a informação não está na tabela.

Se precisar fazer cálculos, utilize somente dados da tabela.
"""

import pymysql
from connection import conn

def criar_conversa():
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversas (titulo)
        VALUES ('')
    """)

    conn.commit()

    conversa_id = cursor.lastrowid

    cursor.execute("""
        UPDATE conversas
        SET titulo = %s
        WHERE id = %s
    """, (f"Chat {conversa_id}", conversa_id))

    conn.commit()

    cursor.close()

    return conversa_id

def listar_conversas():
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
        SELECT id, titulo
        FROM conversas
        ORDER BY criado_em DESC
    """)

    data = cursor.fetchall()

    cursor.close()

    return data

def carregar_chat(conversa_id):
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("""
        SELECT emissor, mensagem
        FROM chats
        WHERE conversa_id = %s
        ORDER BY data_envio
    """, (conversa_id,))

    data = cursor.fetchall()

    cursor.close()

    return data

def salvar_msg(conversa_id, emissor, mensagem):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO chats (conversa_id, emissor, mensagem)
        VALUES (%s, %s, %s)
    """, (conversa_id, emissor, mensagem))

    conn.commit()

    cursor.close()

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.write("Chats")

    if st.button(
        "➕ Novo chat",
        use_container_width=True
    ):
        st.session_state.conversa_id = criar_conversa()
        st.session_state.messages = []

    st.divider()

    conversas = listar_conversas()

    for conversa in conversas:
        if st.button(
            conversa["titulo"],
            key=conversa["id"],
            use_container_width=True
        ):
            st.session_state.conversa_id = conversa["id"]

            dados = carregar_chat(conversa["id"])

            st.session_state.messages = [
                {
                    "role": msg["emissor"],
                    "content": msg["mensagem"]
                }
                for msg in dados
            ]

pergunta = st.chat_input("Faça uma pergunta...")

if "conversa_id" not in st.session_state:
    st.session_state.conversa_id = None

if pergunta:

    if st.session_state.conversa_id is None:
        st.session_state.conversa_id = criar_conversa()

    st.session_state.messages.append({
        "role": "user",
        "content": pergunta
    })

    mensagens = [
        {
            "role": "system",
            "content": system_prompt
        }
    ] + st.session_state.messages

    salvar_msg(
        st.session_state.conversa_id,
        "user",
        pergunta
    )

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=mensagens,
        temperature=0.2
    )

    texto = resposta.choices[0].message.content

    st.session_state.messages.append({
        "role": "assistant",
        "content": texto
    })

    salvar_msg(
        st.session_state.conversa_id,
        "assistant",
        texto
    )

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
    