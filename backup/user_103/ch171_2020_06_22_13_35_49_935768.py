class Carrinho():
    def __init__(self):
        self.valor= {}

    def adiciona(self,nome_produto,preco):
        if nome_produto not in self.valor:
            self.valor[nome_produto] = preco
        else: 
            self.valor[nome_produto]+= preco

    def total_do_produto(self,nome_produto):
        return self.valor[nome_produto]

    



        