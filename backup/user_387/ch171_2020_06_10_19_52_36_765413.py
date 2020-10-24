class Carrinho():
    def __init__(self):
        self.dic ={}

    def adiciona(self, nome_produto, preco):
        if nome_produto not in dic:
            dic[nome_produto] = preco

        else:
            dic[nome_produto]+=preco

    def total_do_produto(self, nome_produto):
        dic[nome_produto]