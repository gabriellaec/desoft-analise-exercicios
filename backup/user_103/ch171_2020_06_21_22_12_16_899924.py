class Carrinho:
    def __init__(self,adiciona,total_do_produto):
        self.adiciona = adiciona
        self.total_do_produto= {}

        def adiciona(self,nome_do_produto,preco):
            self.nome_produto= nome_produto
            self.preco = preco
            if nome_produto not in total_do_produto:
                total_do_produto[nome_produto] = preco
            else: 
                total_do_produto[nome_produto]+= preco
        
        def total_do_produto(self,nome_produto):
            return total_do_produto[nome_produto]
            
        

        