class Carrinho:
    d = {}
    def adiciona(self, item_preco, item_nome):
        self.d[item_nome] = item_preco
    def total(self):
        for i in self.d.values():
            total+=i
        return total