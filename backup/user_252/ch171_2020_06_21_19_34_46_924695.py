class Carrinho:
    def __init__(self):
        self.dicio={}
 
    def adiciona(self, nome_produto, preco):
        self.dicio[nome_produto] = preco
 
    def total(self, nome produto):
        return sum([i for i in self.dicio.values()])