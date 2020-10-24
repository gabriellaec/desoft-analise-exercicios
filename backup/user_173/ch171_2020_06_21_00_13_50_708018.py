class Carrinho:
    def __init__(self,dic):
        self.dic = dic
        dic = {}
    def adiciona(self,nome_produto,preco):
        preco = self.dic[nome_produto]
        
    def total_do_produto(self,nome_produto):
        return self.dic[nome_produto]
        