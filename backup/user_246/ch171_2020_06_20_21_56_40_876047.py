class Carrinho:
    def __init__(self):
        self.car = {}
    def adiciona(self, nome_produto, preco):
        if nome_produto in car:
            self.car[nome_produto] += preco
        
        
    def total_do_produto(self, nome_produto): 
        return (self.car[nome_produto])
        
    