def apaga_repetidos(texto):
    repetido = []
    for i in texto:
        if i in repetido:
            i.replace(i, '*')
        repetido.append(i)
    return texto