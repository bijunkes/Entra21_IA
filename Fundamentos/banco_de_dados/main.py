import pymysql

conexao = pymysql.connect(
    host="localhost",
    user="root",
    passwd="admin",
    port=3306,
    database="loja"
)

# cursor = conexao.cursor()
# sql = '''select * from produtos'''
# cursor.execute(sql)
# produtos = cursor.fetchall()
# for produtos in produtos:
#     print(produtos)

cursor = conexao.cursor()
sql = '''INSERT INTO produtos (nome, preco , qtde, id) VALUES (%s, %s, %s, %s)'''
valores = ('modem', 100, 500, 5)
cursor.execute(sql, valores)
conexao.commit()