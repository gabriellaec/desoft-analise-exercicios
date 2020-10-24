class Carrinho:
    
    def __init__(self):
        self.t = dict()

    def adiciona(self, nome_produto, preco):
        self.t['nome_produto'] = preco

    def total_do_produto(self, nome_produto):
        for i in self.t.values():
              return sum([i])


            
        