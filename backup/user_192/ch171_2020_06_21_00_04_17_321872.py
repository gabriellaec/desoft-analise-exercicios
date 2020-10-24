class Carrinho:
    def __init__(self):
        self.d = dict()
        
    def adiciona(self, nome_produto, preco):
        if not nome_produto in d.keys():
            self.d[nome_produto] = preco
        else:
            self.d[nome_produto] += preco
        return self.d
    
    def total_do_produto(self, nome_produto):
        return self.d[nome_produto]