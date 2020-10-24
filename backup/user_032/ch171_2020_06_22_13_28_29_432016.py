class Carrinho:
    def __init__(self):
        self.produtos = {}
    def adiciona(self, nome_produto, preco):
        if nome_produto in self.produtos:
            self.produtos[nome_produto] += preco
        else:
            self.produto[nome_produto] = preco
    def total_do_produto(self, nome_produto):
        return self.produtos[novo_produto]