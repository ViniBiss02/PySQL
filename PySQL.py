import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Vi_capivara_9',
    database='bdyoutube',
)
cursor = conexao.cursor()

#CRUD
nome_produto = "todynho"
comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit() # edita o banco de dados


cursor.close()
conexao.close()

# CREATE______________________________________________________________________
#nome_produto = "chocolate"
#valor = 15
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)

# READ________________________________________________________________________
#comando = f'SELECT * FROM vendas;'
#cursor.execute(comando)
#resultado = cursor.fetchall() # ler o banco de dados
#print(resultado)

# UPDATE______________________________________________________________________
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados

# DELETE______________________________________________________________________
#nome_produto = "todynho"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() # edita o banco de dados