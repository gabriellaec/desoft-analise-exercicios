def conta_letras(palavra):
    letras = {}
    for i in palavra:
        if i not in letras:
            letras[i] = 1
        else:
            letras[1]+=1
    return letras