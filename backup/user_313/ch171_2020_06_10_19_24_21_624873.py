class Carrinho:
    
    def __init__ (self):
        
        self.dict = {}
        
    def adiciona(self, nome_produto, preco ):
        self.produto = nome_produto
        self.preco = preco
        
        if self.produto not in self.dict:
            self.dict[self.produto] = self.preco
        
        else:
            self.dict[self.produto] += self.preco
    
    
    def total_do_produto(self, nome_produto):
        
        self.soma = self.dict[nome_produto]
        return self.soma