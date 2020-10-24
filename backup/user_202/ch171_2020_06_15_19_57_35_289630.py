class Carrinho():
    def __init__(self):
        self.produtos = {}
    def adiciona(self, produto, valor):
        if produto in self.produtos:
            produtos[produto] += valor
        else:
            produtos[produto] = valor
    def total_do_produto(self, produto):
        return self.produtos[produto]