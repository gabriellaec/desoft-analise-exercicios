class Carrinho: 
    def __init__(self):
        self.carrinho = {}
    def adiciona (self, nome_produto, preco):
        if nome_produto not in self.carrinho.keys():
            self.carrinho[nome_produto] = preco
        else:
            self.carrinho[nome_produto] += preco
        
    def total_do_produto(self, nome_produto):
        return self.carrinho[nome_produto]