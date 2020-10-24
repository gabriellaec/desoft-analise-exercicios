class Carrinho:
    def __init__(self):
        self.dicio={}

    def adiciona(self, nome_produto, preco):
        for k, v in self.dicio.items():
            if k==nome_produto and v!=0:
                self.dicio[nome_produto]+=int(preco)
            elif k==nome_produto and v==0:
                self.dicio[nome_produto]=int(preco)

    def total_do_produto(self, nome_produto):
        return self.dicio[nome_produto]
            