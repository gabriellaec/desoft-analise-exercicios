class Carrinho:
    def __init__(self):
        dicio={}

    def adiciona(self, nome_produto, preco):
        for i in self.dicio.keys():
            if i==self.nome_produto:
                self.dicio[i]=self.dicio[i]+self.preco
        self.dicio[self.nome_produto]=self.preco
        
    def total_do_produto(self, nome_produto):
        return self.dicio[self.nome_produto]