class Carrinho:
    def __init__(self):
        self.dic = {}
    
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dic.keys():
            self.dic[nome_produto] = preco
        else:
            self.dic[nome_produto] += preco

    def total_do_produto(self, nome_produto):
        return self.dic[nome_produto] 