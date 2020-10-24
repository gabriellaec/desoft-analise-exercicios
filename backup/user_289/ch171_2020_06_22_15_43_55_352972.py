class Carrinho:
    def __init__(self):
        self.dicionario = dict()
    def adiciona(self, nome_produto, preco): 
        if nome_produto not in self.dicionario.keys():
            self.dicionario[nome_produto] = preco
        else:
            self.dicionario[nome_produto] += preco
    def total_do_produto(self, nome_produto):
        preco = self.dicionario[nome_produto]
        return preco