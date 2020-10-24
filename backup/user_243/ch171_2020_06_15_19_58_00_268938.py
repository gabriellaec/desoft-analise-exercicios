class Carrinho:
    def __init__(self):
        self.produtos = {}
    
    def adiciona(self,produto, valor):
        if produto in self.produtos:
            self.produtos[produto] += valor
        else:
            self.produtos[produto] = valor
        
    def total_do_produto(self,produto):
        return self.produtos[produto]
        
    