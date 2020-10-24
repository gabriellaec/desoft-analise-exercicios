class Carrinho:
    def __init__(self):
        self.dict = {}
    def adiciona(self, nome_produto, preco):
        if nome_produto not in self.dict:
            self.dict[nome_produto] = preco
        else:
            novo_preco = self.dict[nome_produto]
            self.dict[nome_produto] = (novo_preco + preco)
    def total_do_produto(self, nome_produto):
        return self.dict[nome_produto]
    
            
        
        