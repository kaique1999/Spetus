
import sqlite3


class Cliente:
    with sqlite3.connect("Cliente.db") as con:
        cursor = con.cursor()
        cursor.execute(""" Create Table if not exists Cliente(
                        id_pedido integer primary key autoincrement,
                        nome_cliente varchar(30) not null,
                        status integer not null
                            )""")

    def Cadastrar_Cliente(nome, pago):
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            cursor.execute(
                "insert into Cliente (nome_cliente, status) values(?, ?)", (nome, pago,))
            con.commit()

    def Clientes():
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            return cursor.execute("select * from Cliente")
            con.commit()

    def Pesquisar_ClienteId(id_cliente):
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            return cursor.execute("Select * from Cliente where id_pedido = ?", (id_cliente,))
            con.commit()

    def Pesquisar_ClienteNome(nome_cliente):
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            return cursor.execute("Select * from Cliente where nome_cliente = ?", (nome_cliente,))
            con.commit()

    def Excluir_Cliente(nome_cliente):
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            return cursor.execute("delete from Cliente where id_pedido = ?", (nome_cliente,))
            con.commit()

    def Pagar_Pedido(id_pedido):
        with sqlite3.connect("Cliente.db") as con:
            cursor = con.cursor()
            return cursor.execute("update  Cliente set status = 1 where id_pedido = ? ", (id_pedido,))
            con.commit()
