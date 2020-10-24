class Carrinho:
    def __init__(self):
        self.lista = {}
        pass
    
    def adiciona(self, produto, preco):
        if produto in lista:
            self.lista[produto] += preco
        else:
            self.lista[produto] = preco
    
    def total_do_produto(self, produto):
        return self.lista[produto]