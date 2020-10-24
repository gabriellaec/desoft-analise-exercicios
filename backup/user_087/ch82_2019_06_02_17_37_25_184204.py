def primeiras_ocorrencias(palavra):
    letra_indice = dict()
    lista = []
    for letra in palavra:
        lista.append(letra)
        i = 0 
        while i < len(lista):
             letra = lista[i]
             if letra in letra_indice:
                 letra_indice[letra] = i
             i += 1
    return letra_indice