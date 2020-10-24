class Carrinho:
    def __init__(self):
        self.estoque = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.estoque:
            self.estoque[nome_produto] = preco
        else:
            self.estoque[nome_produto] += preco 
        return self.estoque
    
    def total_do_produto(self, nome_produto):
        a = print(self.estoque[nome_produto])
        return a