Class Carrinho:
    def __init__(self):
        dicionario = {}
    def adiciona(self, nome_produto, preco): 
        if nome_produto not in dicionario:
            dicionario[nome_produto] = preco
        else:
            dicionario[nome_produto] += preco
    def total_do_produto(self, nome_produto):
        preco = dicionario[nome_produto]
        return preco