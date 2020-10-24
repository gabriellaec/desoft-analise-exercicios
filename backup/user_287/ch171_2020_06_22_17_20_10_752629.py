class Carrinho:
    
    def __init__(self):
        self.t = dict()

    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.t:
            self.t[nome_produto] = preco
        else:
            self.t[nome_produto] += preco

    def total_do_produto(self, nome_produto):
        return self.t[nome_produto]





            
        