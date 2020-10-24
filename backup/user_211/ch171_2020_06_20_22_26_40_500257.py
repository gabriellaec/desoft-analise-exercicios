class Carrinho:
    def __init__(self):
        self.dic={}
    def adiciona(self,nome_produto,preco):
        self.dic.setdefault(nome_produto,[]).append(preco)
    def total_do_produto(self,nome_produto):
        return sum(self.dic[nome_produto])
