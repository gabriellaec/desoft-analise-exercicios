class Carrinho:
    def __init__(self):
        self.compras = {}

    def adiciona (self, nome_produto, preco):
        for keys in self.compras:
            if keys == nome_produto:
                self.compras[nome_produto] += preco
            else:
                self.compras[nome_produto] = preco

        """ Esse método deve dar certo. Mas há outra maneira mais direta checar se a Key está no dicionário:
        if nome_produto in compras:
            compras[nome_produto] += preco
        else:
            compras[nome_produto] = preco """

    def total_do_produto (self, nome_produto):
        print (self.compras[nome_produto])