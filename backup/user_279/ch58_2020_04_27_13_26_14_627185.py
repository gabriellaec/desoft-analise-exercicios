palavra = "arara"
def conta_a(palavra):
    lista_a = []
    for i in palavra.itens():
        if palavra[i] == 'a':
            lista_a.append(palavra[i])
            i = i+1
        else:
            i = i+1
    return lista_a