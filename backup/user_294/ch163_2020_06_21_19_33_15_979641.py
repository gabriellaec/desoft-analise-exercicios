def calcula_media (lista):
    notas = []
    for dicionario in lista:
        for valore in dicionario.values():
            notas.append(valore)
    x = sum(notas)/len(notas)
    return x