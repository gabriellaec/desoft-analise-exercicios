class Carrinho():
    def __init__(self):
        self.dicio={}


    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dicio.keys():
            self.dicio[nome_produto]=[]
        self.dicio[nome_produto].append(preco)


    def total_do_produto(self, nome_produto):
        return sum(self.dicio[nome_produto])
