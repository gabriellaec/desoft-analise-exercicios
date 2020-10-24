class Carrinho:
    def __init__(self):
        self.dicio = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto in dicio:
            self.dicio[nome_produto] += preco
        else:
            self.dicio[nome_produto] = preco
            
    def total_do_produto(self, nome_produto):
        total = dicio[nome_produto]
        return total