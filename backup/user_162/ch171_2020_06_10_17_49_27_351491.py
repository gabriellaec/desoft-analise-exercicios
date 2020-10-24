class Carrinho():
    def __init__(self):
        self.dic = {}
        
    def adiciona(self, nome_produto, preco):
        self.dic[nome_produto] = preco
        print(self.dic)
        for np, p in self.dic.items():
            if np == nome_produto:
                self.dic[np] = preco + p
            else:
                self.dic[nome_produto] = preco
    
         
    def total_do_produto(self, nome_produto):
        return self.dic[nome_produto]