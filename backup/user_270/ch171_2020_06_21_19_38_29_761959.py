class Carrinho:
    def __init__(self):
        self.compra = {}
    def adiciona(self, nome_produto, preco):
        self.preco = preco
        self.nome_produto = nome_produto
        self.compra[self.nome_produto] = self.preco
    def total_do_produto(self, nome_produto):
        self.nome_produto = nome_produto
        self.compra[self.nome_produto] += self.nome_produto