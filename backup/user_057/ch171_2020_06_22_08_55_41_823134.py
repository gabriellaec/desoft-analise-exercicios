class Carrinho:
    def __init__(self):
        dic = {}
    def adiciona(self, nome_produto, preco):
        dic = dic
        if nome_produto in dic.keys():
            dic[nome_produto] += preco
        else:
            dic[nome_produto] = preco
        
    def total_do_produto(self, nome_produto):
        return dic[nome_produto]