dicio={}
class Carrinho():
    def __init__(self): 
        pass

    def adiciona(self, nome_produto, preco):
        if nome_produto in dicio.keys():
            dicio[nome_produto]+=preco
        else:
            dicio[nome_produto]=preco
            
    def total_do_produto(self, nome_produto):
        return dicio[nome_produto]