class Carrinho:
    def __init__(self):
        self.dicionario = {}
    def adiciona(self,nome_produto,preco):
        self.nome_produto = nome_produto
        self.preco = preco
        if nome_produto in self.dicionario.keys():
            self.dicionario[nome_produto] = self.dicionario[nome_produto] + self.preco
        else:
            self.dicionario[nome_produto] = preco
    def total_do_produto(self,nome_produto):
        return self.dicionario[self.nome_produto]
    