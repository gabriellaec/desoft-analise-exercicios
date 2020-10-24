class Carrinho:
    def __init__(self):
        d = dict()
        
    def adiciona(self, nome_produto, preco):
        if preco in d[nome_produto]:
            d[nome_produto] += preco
        else:
            d[nome_produto] = preco
    
    def total_do_produto(self, nome_produto):
        return d[nome_produto]