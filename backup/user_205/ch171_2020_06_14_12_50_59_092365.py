class Carrinho():
    def __init__ (self):
        self.dicionario = {}

    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dicionario:
            self.dicionario[nome_produto] = preco
        else:
            self.dicionario[nome_produto] += preco

    def total_do_produto(self, nome_produto):
        for keys in self.dicionario:
            if nome_produto == keys:
                return self.dicionario[keys]