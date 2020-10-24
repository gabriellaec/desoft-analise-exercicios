class Carrinho:
    def __init__(self):
        self.d = dict()
        
    def adiciona(self, nome_produto, preco):
        if self.d[nome_produto] != 0:
            self.d[nome_produto] += preco
        else:
            self.d[nome_produto] = preco
    
    def total_do_produto(self, nome_produto):
        return sum(self.d[nome_produto])