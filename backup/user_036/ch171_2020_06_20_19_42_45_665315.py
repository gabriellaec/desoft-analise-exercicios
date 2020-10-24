class Carrinho:
    d = {}
    def adiciona(self, nome_produto, preco):
        self.d[nome_produto] = preco
    def total_do_produto(self, nome_produto):
        for i in self.d.values():
            total_do_produto+=i
        return sum([i for i in self.d.values()])