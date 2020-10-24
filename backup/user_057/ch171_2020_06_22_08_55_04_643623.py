class Carrinho:
    dic = {}
    def __init__(self):
        
    def adiciona(self, nome_produto, preco):
        if nome_produto in dic.keys():
            dic[nome_produto] += preco
        else:
            dic[nome_produto] = preco
        
    def total_do_produto(self, nome_produto):
        return dic[nome_produto]