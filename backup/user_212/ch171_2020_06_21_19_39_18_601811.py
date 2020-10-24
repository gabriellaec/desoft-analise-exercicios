class Carrinho ():
    
    def __init__(self):
        self.comidas = {}
        
    def adiciona(self, nome_produto, preco):
        if  nome_produto in self.comidas.keys():
            self.comidas[nome_produto] += preco
            
        if nome_produto not in self.comidas.keys():
            self.comidas[nome_produto] = preco
        
    def total_do_produto (self, nome_produto):
        return self.comidas[nome_produto]
        