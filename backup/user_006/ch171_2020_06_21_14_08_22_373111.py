class Carrinho:
    def __init__(self):
        dicio={}
        self.di=dicio
    def adiciona(self, nome_produto, preco):
        encontrou=False
        self.preco=preco
        self.nomep=nome_produto
        for i in self.di.keys():
            if i==self.nomep:
                self.di[i]=self.di[i]+self.preco
                encontrou=True
                break
        if not encontrou:
            self.di[self.nomep]=self.preco
        
    def total_do_produto(self, nome_produto):
        self.nomep=nome_produto
        return self.di[self.nomep]