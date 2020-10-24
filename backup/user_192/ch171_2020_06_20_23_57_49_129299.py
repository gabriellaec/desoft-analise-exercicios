class Carrinho:
    def __init__(self):
        self.d = dict()
        
    def adiciona(self, nome_produto, preco):
        if preco in self.d[nome_produto]:
            self.d[nome_produto] += self.novo_preco
        else:
            self.d[nome_produto] = preco
    
    def total_do_produto(self, nome_produto):
        return sum(self.d[nome_produto])