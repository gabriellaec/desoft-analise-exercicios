class Carrinho:
    def __init__(self):
        self.dicio={}

    def adiciona(self, nome_produto, preco):
        self.valores=self.dicio.values()
        if self.dicio[nome_produto].values()!=0:
            self.dicio[nome_produto]+=preco
        else:
            self.dicio[nome_produto]=preco


    def total_do_produto(self, nome_produto):
        return self.dicio[nome_produto]
            