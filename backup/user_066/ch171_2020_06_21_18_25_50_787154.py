class Carrinho:
    def __init__(self):
        dicionario = {}
        self.dicionario = dicionario
    def adiciona(self, nome_produto, preco):
        if nome_produto in dicionario:
            dicionario[nome_produto] += preco
        else:
            dicionario[nome_produto] = preco
    def total_do_produto(self, nome_produto):
        print(dicionario[nome_produto])