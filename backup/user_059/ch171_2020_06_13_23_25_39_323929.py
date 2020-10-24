class Carrinho:
    def __init__(self):
        self.d = {}

    def adiciona(self, nome_produto, preco):
        l = self.d.keys()
        if nome_produto in l:
            self.d[nome_produto] += preco
        else:
            self.d[nome_produto] = preco

    def total_do_produto(self, nome_produto):
        print(self.d.get(nome_produto))
