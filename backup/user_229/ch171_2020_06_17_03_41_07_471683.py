class Carrinho:
    def __init__(self):
        produto_preco = {}
        
    def adiciona(self, nome_produto, preco):
        if nome_produto in produto_preco:
            produto_preco(nome_produto) += preco
        else:
            produto_preco(nome_produto) = preco
        
    def total_do_produto(self, nome_produto):
        return produto_preco(nome_produto)
                         