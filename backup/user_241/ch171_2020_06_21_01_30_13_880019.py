class Carrinho:
    def __init__(self):
        dicionario = {}
        
    def adiciona(self,nome_produto,preco):
        valor = dicionario.get(nome_produto, 0)
        valor += preco
        dicionario[nome_produto] = valor
        
    def total_do_produto(self, nome_produto):
        return dicionario[nome_produto]
        
       
        
