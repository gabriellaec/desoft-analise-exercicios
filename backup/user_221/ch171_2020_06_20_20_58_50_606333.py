class Carrinho:
    def __init__(self):
        self.dicionario = {}
    def adiciona(self, nome_produto, preco):
        self.nome_produto = nome_produto
        self.preco = preco
        if not self.nome_produto in self.dicionario.keys():
            self.dicionario[self.nome_produto] = self.preco
        else:
            self.dicionario[self.nome_produto] += self.preco
        return self.dicionario
    def total_do_produto(self, nome_produto):
        self.nome_produto = nome_produto
        return self.dicionario[self.nome_produto]
            
    