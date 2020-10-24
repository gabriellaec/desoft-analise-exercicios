class Carrinho:
    def __init__(self):
        self.dic = {}
        
    def adiciona(self,produto,preco):
        if produto in self.dic:
            self.dic[produto] += valor
        else:
            self.dic[produto] = valor
            
    def total_do_produto(self,nome_produto):
        return self.dic[produto]
        