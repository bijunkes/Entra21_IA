import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='senha',
    port=3306,
    database='producao'
)