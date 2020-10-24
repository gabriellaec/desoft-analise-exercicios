def apaga_repetidos(texto):
    repetido = []
    novo = ''
    for i in texto or i.upper() in repetido:
        if i in repetido:
            troca = i.replace(i, '*')
            novo += troca
        else:
            novo += i
        repetido.append(i)
    return novo