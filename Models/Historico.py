import sqlite3


class Historico:
    with sqlite3.connect("Historico.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""Create Table if not exists Historico(
                            id integer primary key autoincrement,
                            nome_cliente varchar(50) not null,
                            valor_total varchar(10) not null,
                            data_pedido varchar(20) not null)
                        """)

    def Adicionar_Vendas(nome_cliente, valor_total, data_pedido):
        with sqlite3.connect("Historico.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""insert into Historico (nome_cliente, valor_total, data_pedido)
                                values (?, ?, ?) """, (nome_cliente, valor_total, data_pedido))
            conn.commit()

    def Retornar_Historico():
        with sqlite3.connect("Historico.db") as conn:
            cursor = conn.cursor()    
            return cursor.execute("select * from Historico")   
            conn.commit()
    
    def Delete_Venda(id_venda):
        with sqlite3.connect("Historico.db") as conn:
            cursor = conn.cursor()
            cursor.execute("delete from Historico where id = ?", (id_venda, ))
        conn.commit()
