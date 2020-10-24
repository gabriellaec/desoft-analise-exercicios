class Carrinho():
    def __init__(self): 
        self.carte={}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto in self.carte.keys():
            self.carte[nome_produto]+=preco
        else:
            self.carte[nome_produto]=preco
            
    def total_do_produto(self, nome_produto):
        return self.carte[nome_produto]