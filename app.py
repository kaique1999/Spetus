from flask import Flask, render_template, redirect, jsonify, url_for, request
from Models.Estoque import Estoque
from Models.Cliente import Cliente
from Models.Itens_pedido import Itens
from Models.Historico import Historico
from datetime import datetime

app = Flask(__name__)


@app.route("/Estoque")
def estoque():
    return render_template('estoque.htm', titulo="Estoque", produtos=Estoque.Produtos())


@app.route("/Estoque", methods=["POST"])
def EntradaEstoque():
    nome = request.form["nome"]
    quantidade = request.form["quantidade"]
    preco = request.form["preco"]
    preco_pg = request.form["preco_pg"]
    if nome == None or nome == "":
        return redirect(url_for("estoque"))
    produto = Estoque.Cadastrar(str(nome), int(
        quantidade), str(preco), str(preco_pg))
    return redirect(url_for("estoque"))


@app.route("/Estoque/<id>")
def excluir(id):
    Estoque.Delete(id)
    return redirect(url_for("estoque"))


@app.route("/")
@app.route("/Pedido")
def comandas():
    return render_template('pedido.htm', titulo="Pedido", cliente=Cliente.Clientes())


@app.route("/Pedido", methods=["POST"])
def clientes():
    nome = request.form["nome"]
    if nome == None or nome == "":
        return redirect(url_for("comandas"))
    Cliente.Cadastrar_Cliente(str(nome), int(0))
    return redirect(url_for("comandas"))

@app.route("/Pedido/<id>/Excluir")
def Excluir_Comanda(id):
    for id in Cliente.Pesquisar_ClienteId(id):
        Cliente.Excluir_Cliente(id[0])
        return redirect(url_for("comandas"))

@app.route("/Pedido/<id>")
def get_pedido(id):
    for nome in Cliente.Pesquisar_ClienteId(id):
        titulo = nome[1]
    total = 0
    for itens in Itens.Filtrar_Itens(id):
        for produto in Estoque.Pesquisar_ProdutoId(itens[2]):
            total = total + float(produto[3].replace(",", "."))
    return render_template("pedido_cliente.htm", titulo=titulo, id=id, Estoque=Estoque, Cliente=Cliente, Itens=Itens, total=total)


@app.route("/Pedido/<id>", methods=["POST"])
def Return_produtos(id):
    produto = request.form['produtos']
    for id_produto in Estoque.Pesquisar_Produto(produto):
        Estoque.Editar_Quantidade(id_produto[2]-1, id_produto[0])
        Itens.Itens_Pedido(id, id_produto[0])
    return redirect(url_for("get_pedido", id=id))

@app.route("/Pedido/<id>/ExcluirItem")
def Excluir_Item(id):
    for nome in Itens.Filtrar_ItensIdItem(id):
        id_pedido = nome[1]
        for estoque in Estoque.Pesquisar_ProdutoId(nome[2]):
            Estoque.Editar_Quantidade(estoque[2]+1 ,nome[2])
            Itens.Excluir_ItemIdProduto(id)
    return redirect(url_for("get_pedido", id=nome[1]))


@app.route("/Historico")
def return_historico():
    return render_template("historico.htm", Historico=Historico, titulo="Historico")

@app.route("/Historico/<id>")
def Delete_Venda(id):
    Historico.Delete_Venda(id)
    return redirect(url_for('return_historico'))


@app.route("/Pedido/<id>/<valor_total>/Pago")
def Pagar_Pedido(id, valor_total):
    date = datetime.now()
    Cliente.Pagar_Pedido(id)
    if float(valor_total) > 0:
        for valores in Cliente.Pesquisar_ClienteId(id):
            Historico.Adicionar_Vendas(str(valores[1]), str(valor_total), date )
        return redirect(url_for("comandas"))
    return redirect(url_for("get_pedido", id=id))

@app.route("/Editar/<id>")
def Editar_Estoque(id):
    return render_template("editar_estoque.htm", id=id, titulo="Editar Estoque", Estoque=Estoque)

@app.route("/Editar/<id>", methods=["POST"])
def Salvar_Edicao(id):
    nome = request.form['nome']
    quantidade = request.form['quantidade']
    preco = request.form['preco']
    preco_pg = request.form['preco_pg']
    if nome and quantidade and preco and preco_pg:
        Estoque.Editar_Estoque(nome, quantidade, preco, preco_pg, id)
    return redirect(url_for("estoque"))

if __name__ == '__main__':
    app.run(debug=True)
