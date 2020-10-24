class Carrinho:
    def __init__(self):
        dicio={}
        self.di=dicio
    def adiciona(self, nome_produto, preco):
        self.preco=preco
        self.nomep=nome_produto
        self.di=dicio
        for i in dicio.keys():
            if i==nome_produto:
                dicio[i]=dicio[i]+preco
        dicio[nome_produto]=preco
        
    def total_do_produto(self, nome_produto):
        self.nomep=nome_produto
        return dicio[nome_produto]