class Carrinho():
    def __init__(self):
        self.dic = {}
    def adiciona(self,nome_produto,preco):
        if nome_produto in self.dic:
            preco_atual = self.dic[nome_produto]
            self.dic[nome_produto] =  (preco+preco_atual)
        else:
            self.dic[nome_produto] = preco
    def total_do_produto(self, nome_produto):
        return self.dic[nome_produto]