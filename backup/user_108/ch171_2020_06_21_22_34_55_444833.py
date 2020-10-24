class Carrinho:
    def __init__(self):
        self.produtos = dict()
        
    def adiciona(self, nome_produto, preco):
        self.produtos[nome_produto] = self.produtos.get(nome_produto,[]) + [preco]
        
    def total_do_produto(self, nome_produto):
        if nome_produto in self.produtos:
            return sum(self.produtos[nome_produto])