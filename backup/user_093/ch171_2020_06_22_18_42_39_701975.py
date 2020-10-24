class Carrinho:
    def __init__(self):
        self.dic={}
    def adiciona(self,nome_produto,preco):
        if not nome_produto in self.dic:
            self.dic[nome_produto]=preco
        else:
            self.dic[nome_produto]+=preco
    def total_de_produto (self,nome_produto):
        return self.dic[nome_produto]
    