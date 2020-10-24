class Carrinho(self):
    def __init__(self):
        self.d={}
    def adiciona(self,nome_produto,preco):
        if nome_produto not in self.d:
            d[nome_produto] = preco
        if nome_produto in self.d:
            d[nome_produto]+=preco
    def total_do_produto(self,nome_produto):
        return d[nome_produto]