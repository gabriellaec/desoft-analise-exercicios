class Carrinho:
    def _init_(self):
        self.car = {}
       
    def adiciona(self,nome_produto,preco):
        if nome_produto not in self.car.keys():
            self.car[nome_produto] = preco
        else:
            self.car[nome_produto] += preco
            
    def total_do_produto(self, nome_produto):
        return self.car[nome_produto]