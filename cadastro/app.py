import streamlit as st
import mysql.connector

# Conexão com o banco
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha",
        database="cadastro_db"
    )

st.title("Cadastro de Usuários")

nome = st.text_input("Nome")
email = st.text_input("Email")

if st.button("Cadastrar"):
    conexao = conectar()
    cursor = conexao.cursor()

    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome, email)

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    st.success("Usuário cadastrado com sucesso!")

    st.subheader("Usuários cadastrados")

conexao = conectar()
cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

for usuario in cursor.fetchall():
    st.write(usuario)

cursor.close()
conexao.close()