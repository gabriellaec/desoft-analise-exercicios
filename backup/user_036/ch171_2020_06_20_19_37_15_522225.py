class Carrinho:
    d = {}
    def adiciona(self, nome_produto, preco):
        self.d[nome_produto] = preco
    def total(self):
        for i in self.d.values():
            total+=i
        return total