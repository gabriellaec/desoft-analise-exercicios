class Carrinho:
    def __init__(self):
        self.dict = {}
    def adiciona(self, nome_produto, preco):
        if nome_produto in self.dict.keys():
            self.dict[nome_produto] += preco
        else:
            self.dict[nome_produto] = preco
    def total_do_produto(self, nome_produto):
        return self.dict[nome_produto]