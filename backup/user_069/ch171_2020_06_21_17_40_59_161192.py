class Carrinho:

    pass

    def __init__(self):
        self.dic = {}

    def adiciona(self, nome_produto, preco):

        if not nome_produto in self.dic:
            self.dic[nome_produto] = preco

        else: 
            self.dic[nome_produto] += preco

        return self.dic

    def total_do_produto(self, nome_produto):

        if nome_produto in self.dic:
            self.total = self.dic[nome_produto]

        return self.total 