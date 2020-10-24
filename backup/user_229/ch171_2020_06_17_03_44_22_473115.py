class Carrinho:
    def __init__(self):
        self.produto_preco = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto in self.produto_preco:
            self.produto_preco[nome_produto] += preco
        else:
            self.produto_preco[nome_produto] = preco
        
    def total_do_produto(self, nome_produto):
        return self.produto_preco[nome_produto]
                         