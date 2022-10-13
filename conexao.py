import mysql.connector

class Conexao:

    def __init__(self,host,dbname,user,password):
        self.host = host
        self.database = dbname
        self.user = user
        self.password = password
        global conn

        conn = mysql.connector.connect(host=self.host,database=self.database,user=self.user,password=self.password)

        try:
            if( conn.is_connected ):
                print('conectado')

        except:
            print('Erro') 

    def listaProdutos(self):
        cursor = conn.cursor()
        cursor.execute('SELECT id_produto, nome_produto FROM produtos;')
        linhas = cursor.fetchall()
        print("Total de registros: " + str(cursor.rowcount))
        for linha in linhas:
            print(str(linha[0]) + '- ' + linha[1])

    def insereProdutos(self,value):
        cursor = conn.cursor()
        cursor.execute('INSERT INTO produtos (nome_produto) VALUES ("' + value + '");')
        conn.commit()
        print('Produto cadastrado')

    def excluirProdutos(self,id):
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id_produto = ' + str(id) + ';')
        conn.commit()
        print('Produto excluido')

    def alterarProdutos(self,value,id):
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET nome_produto = "' + value + '" WHERE id_produto = ' + str(id) + ';')
        conn.commit()



conexao = Conexao('localhost','lojapython','root','') 
#conexao.listaProdutos()
#conexao.insereProdutos()
#conexao.excluirProdutos()
#conexao.alterarProdutos('Teclado', 1)