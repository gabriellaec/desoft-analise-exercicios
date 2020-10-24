class Carrinho:
    def __init__(self):
        compras = {}

    def adiciona (self, nome_produto, preco):
        for keys in compras:
            if keys == nome_produto:
                compras[nome_produto] += preco
            else:
                compras[nome_produto] = preco

        """ Esse método deve dar certo. Mas há outra maneira mais direta checar se a Key está no dicionário:
        if nome_produto in compras:
            compras[nome_produto] += preco
        else:
            compras[nome_produto] = preco """

    def total_do_produto (self, nome_produto):
        return compras[nome_produto]