class Carrinho:
    def __init__(self):
        car = {}
    def adiciona(self, nome_produto, preco):
        car[nome_produto] = preco
        
        
    def total_do_produto(self, nome_produto):
        print car[nome_produto]
        
    