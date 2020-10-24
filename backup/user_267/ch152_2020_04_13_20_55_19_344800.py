titulo = input('Didite o titulo do livro: ')

def verifica_preco(titulo, dcores, dprecos):
    if titulo in dcores:
        cor = dcores[titulo]
        if cor in dprecos:
            preco = dprecos[cor]
    return preco
    