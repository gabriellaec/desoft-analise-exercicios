class Carrinho:
    def __init__(self):
        self.dicio={}
        
    def adiciona(self, nome_produto, preco):
        for i in dicio.keys():
            if i==nome_produto:
                dicio[i]=dicio[i]+preco
        dicio[nome_produto]=preco
        
    def total_do_produto(self, nome_produto):
        return dicio[nome_produto]