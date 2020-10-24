class Carrinho:
    t = {}

    def adiciona(self, item_preco, item_nome):
        self.t[item_nome] = item_preco

    def total(self):
        '''total = 0 
        for i in self.t.values():
            total+=i
        return'''
        return sum([i for i in self.t.values()])