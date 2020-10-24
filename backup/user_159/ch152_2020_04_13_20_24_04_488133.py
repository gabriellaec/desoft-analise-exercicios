livros = {}
tebeladecores = {}
def verifica_preco(nome,livros,tabeladecores):
    
    if nome in livros:
        cor = livros[nome]
        return tabeladecores[cor]
    else:
        return'esse livro nao existe'
    