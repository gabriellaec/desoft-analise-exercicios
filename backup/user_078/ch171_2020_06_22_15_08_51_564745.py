class Carrinho:
    def __init__(self):
        self.cart = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.cart.keys():
            self.cart[nome_produto] = preco
        else:
            self.cart[nome_produto] += preco
            
    def total_do_produto(self, nome_produto):
        return self.cart[nome_produto]