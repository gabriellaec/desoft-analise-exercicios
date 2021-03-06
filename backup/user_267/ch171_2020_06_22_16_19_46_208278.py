class Carrinho:
    def __init__(self):
        self.dicio = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dicio.keys():
            self.dicio[nome_produto] = preco
        else:
            self.dicio[nome_produto] += preco
            
    def total_do_produto(self, nome_produto):
        preco_total = self.dicio[nome_produto]
        return preco_total
        