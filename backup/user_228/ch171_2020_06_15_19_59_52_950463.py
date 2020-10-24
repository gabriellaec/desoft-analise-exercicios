class Carrinho:
    def __init__(self):
        self.produtos={}
    def adiciona(self, produto, preco):
        if produto in self.produtos:
            self.produtos[produto]+=preco
        else:
            self.produtos[produto]=preco   
    def total_do_produto(self, produto):
        return self.produtos[produto]
    