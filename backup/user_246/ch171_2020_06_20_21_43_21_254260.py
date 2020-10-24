class Carrinho:
    def __init__(self):
        self.car = {}
    def adiciona(self, nome_produto, preco):
        self.car[nome_produto] = preco
        
        
    def total_do_produto(self, nome_produto):
        print (self.car[nome_produto])
        
    