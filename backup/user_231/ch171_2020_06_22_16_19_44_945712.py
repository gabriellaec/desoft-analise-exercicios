class Carrinho:
    def __init__(self):
        self.dicionario={}
    def adiciona(self, nome_produto, preco):
        self.nome_produto= nome_produto
        self.preco= preco
        if self.nome_produto in self.dicionario:
            self.dicionario['nome_produto']+= self.preco
        else:
            self.dicionario['nome_produto']= self.preco
    def total_do_produto(self, nome_produto):
        self.nome_produto= nome_produto
        return self.dicionario['nome_produto']
        
        