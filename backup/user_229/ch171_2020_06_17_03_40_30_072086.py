class Carrinho:
    def __init__(self):
        
    def adiciona(self, nome_produto, preco):
        produto_preco = {}
        if nome_produto in produto_preco:
            produto_preco(nome_produto) += preco
        else:
            produto_preco(nome_produto) = preco
        
    def total_do_produto(self, nome_produto):
        return produto_preco(nome_produto)
                         