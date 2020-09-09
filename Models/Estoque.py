import sqlite3

class Estoque:
    with sqlite3.connect("Estoque.db") as con:
        cursor = con.cursor()
        cursor.execute("""
                        Create Table if not exists Estoque(
                            id integer primary key  autoincrement,
                            nome_produto varchar(50) not null,
                            quantidade integer not null,
                            preco varchar(10) not null,
                            preco_pg varchar(10) not null)
                            """)


    def Cadastrar(produto, quantidade, preco, preco_pg):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            cursor.execute("""insert into Estoque (nome_produto, quantidade, preco, preco_pg)
                         values(?, ?, ?, ?)""", (produto, quantidade, preco, preco_pg))
            con.commit()
            
    
    def Produtos():
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            return cursor.execute("select * from Estoque")
    
    def Delete(id):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            cursor.execute("delete from  Estoque where id = ?", (id,))
            con.commit()

    def Pesquisar_Produto(nome_produto):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            return cursor.execute("Select * from Estoque where nome_produto = ?", (nome_produto,))
    
    def Pesquisar_ProdutoId(id):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            return cursor.execute("Select * from Estoque where id = ?", (id,))
    
    def Editar_Estoque(nome_produto, quantidade, preco, preco_pg, id_produto):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            return cursor.execute("""Update Estoque set nome_produto = ?, quantidade = ?, 
                                    preco = ?, preco_pg = ? where id = ?""", (nome_produto, quantidade, preco, preco_pg, id_produto))
            con.commit()
    
    def Editar_Quantidade(quantidade_produto, id_produto):
        with sqlite3.connect("Estoque.db") as con:
            cursor = con.cursor()
            return cursor.execute("""Update Estoque set quantidade = ? where id = ?""",
                                    (quantidade_produto, id_produto,))
            con.commit()





    
    
    
