class Carrinho:
    def __init__(self):
        self.dicio = {}
        preco_total = 0
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dicio.keys():
            self.dicio[nome_produto] = preco
        else:
            self.dicio[nome_produto] += preco
    def total_do_produto(self, nome_produto):
        for preco in self.dicio.values():
            preco_total += preco
        return preco_total
        