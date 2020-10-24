class Carrinho:
    def __init__(self):
        self.d={}
    def adiciona(self,nome_produto,preco):
        if nome_produto not in self.d:
            self.d[nome_produto] = preco
        else:
            self.d[nome_produto]+=preco
    def total_do_produto(self,nome_produto):
        return self.d[nome_produto]