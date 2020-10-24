class Carrinho:
    t = {}
 
    def adiciona(self, nome_produto, preco):
        self.t[nome_produto] = preco
 
    def total_do_produto(self, nome_produto):
        total = 0
        for i in self.t.values():
            total+=i
        return total