class Carrinho:
    def __init__(self):
        self.compras = {}

    def adiciona (self, nome_produto, preco):
        if nome_produto in self.compras:
            self.compras[nome_produto] += preco
        else:
            self.compras[nome_produto] = preco 

    def total_do_produto (self, nome_produto):
        if nome_produto in self.compras:
            return self.compras[nome_produto]
        else:
            return 0