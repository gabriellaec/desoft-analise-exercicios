class Carrinho:
    def __init__(self):
        self.dici = {}
    
    def adiciona(self, nome_produto, preco):
        li = []
        for i in self.dici.keys():
            li.append(i)
        self.nome_produto = nome_produto
        self.preco = preco
        c = 0
        for a in li:
            if self.nome_produto == a:
                c = li.index(a)+1
        if c == 0:
            self.dici[self.nome_produto] = self.preco
        else:
            count = 1
            k =''
            h = 0
            for a, b in self.dici.items():
                if c == count:
                    k = a
                    h = b
                    print (k)
                    print(h)
                count += 1
            self.dici[k] = h + self.preco 
    def total_do_produto(self, nome_produto):
        return self.dici[nome_produto]