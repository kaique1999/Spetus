import sqlite3

class Itens:
    with sqlite3.connect("Itens_pedido.db") as conn:
        cursor = conn.cursor()
        cursor.execute(""" Create Table if not exists Itens_pedido(
                            id_item integer primary key autoincrement,
                            id_pedido integer not null,
                            nome_item integer not null,
                            foreign key (id_pedido)
                                references Cliente (id_pedido),
                            foreign key (nome_item)
                                references Estoque (id)
                                )""")

    def Itens_Pedido(id_pedido, id_item):
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Itens_pedido(id_pedido, nome_item) values
                                                    (?,?)""", (id_pedido, id_item))
            conn.commit()

    
    def Retornar_Itens():
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Itens_pedido")
            conn.commit()
    
    def Filtrar_Itens(id):
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Itens_pedido where id_pedido = ?", (id,))
            conn.commit()
        
    def Filtrar_ItensIdItem(id_item):
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("Select * from Itens_pedido where id_item = ?", (id_item,))
            conn.commit()
    
    def Excluir_ItemIdPedido(id_cliente):
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("delete from Itens_pedido where id_pedido = ?", (id_cliente,))
            conn.commit()
    
    def Excluir_ItemIdProduto(id_produto):
        with sqlite3.connect("Itens_pedido.db") as conn:
            cursor = conn.cursor()
            return cursor.execute("delete from Itens_pedido where id_item = ?", (id_produto,))
            conn.commit()
    