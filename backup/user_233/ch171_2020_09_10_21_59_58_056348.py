
class Carrinho():
    
    def __init__(self): self.itens = dict()
        
        
    def adiciona(self, nome_produto, preco):
        
        if nome_produto in self.itens.keys():
            self.itens[nome_produto] += preco
        
        else: self.itens[nome_produto] = preco
            
    
    def total_do_produto(self, nome_produto):
        
        return self.itens[nome_produto]

