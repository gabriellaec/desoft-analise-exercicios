class Carrinho:

    def __init__(self):
        self.dicio = dict()

    def adiciona(self, nome_produto, preco):
        self.nome = nome_produto
        self.preco = preco

        if self.nome not in self.dicio.keys():
            self.dicio[self.nome] = self.preco
        else:
            self.dicio[self.nome] += self.preco 

    def total_do_produto(self, nome_produto):
        self.nome = nome_produto

        x = self.dicio[self.nome]

        return x