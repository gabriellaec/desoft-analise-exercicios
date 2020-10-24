class Carrinho:
    def __init__(self):
        self.produtos = {}
    def adiciona(self,produto, valor):
        if produto in self.produtos:
            self.produtos[produto] += valor
        else:
            self.produtos[produto] = valor
    def total_do_produto(self, produto):
        return self.produtos[produto]


c = Carrinho()
c.adiciona('banana', 5)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 5
c.adiciona('abacate', 7)
c.adiciona('banana', 4)
total_banana = c.total_do_produto('banana')
print(total_banana)  # Vai imprimir 9