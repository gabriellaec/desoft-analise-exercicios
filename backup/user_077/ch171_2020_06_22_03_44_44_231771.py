class carrinho:
    def __init__(self):
        itens={}
        self.itens=itens
    def adiciona(self,nome_produto,preco):
        if nome_produto not in self.itens.keys:
            self.itens[nome_produto]=preco
        else:
            self.itens[nome_produto]+=preco
    def total_do_produto(self,nome_produto):
        return self.itens[nome_produto]
    