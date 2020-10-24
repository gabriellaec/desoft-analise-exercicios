class Carrinho:
    def __init__(self):
        self.dicionario = {}
        
    def adiciona(self,nome_produto,preco):
        valor = self.dicionario.get(nome_produto, 0)
        valor += preco
        self.dicionario[nome_produto] = valor
        
    def total_do_produto(self, nome_produto):
        return self.dicionario[nome_produto]
        
       
        
