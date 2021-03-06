class Carrinho:
    def __init__(self):
        self.dic = {}
    
    def adiciona(self, nome_produto, preco):
        try:
            self.dic[nome_produto] += preco
        except Exception as e:
            self.dic[nome_produto] = preco
        
    def total_do_produto(self, nome_produto):
        return self.dic[nome_produto]