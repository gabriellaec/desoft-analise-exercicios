class Carrinho:
    def __init__(self):
        self.compra = {}
    def adiciona(self, nome_produto, preco):
        self.preco = preco
        self.nome_produto = nome_produto
        if nome_produto not in compra :   
            self.compra[nome_produto] = preco
        else:
            compra[nome_produto] += preco
    def total_do_produto(self, nome_produto):
        return compra[nome_produto] 