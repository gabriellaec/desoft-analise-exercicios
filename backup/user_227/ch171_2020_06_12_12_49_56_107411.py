class Carrinho():
    
    def __init__(self):

        self.dicionario = {}
    
    def adiciona(self, nome_produto, preco):

        self.dicionario[self.nome_produto] += self.preco
    
    def total_do_produto(self, nome_produto):

        self.total = sum(self.dicionario[nome_produto])