def calcula_media (lista):
    notas = []
    for dicionarios in lista:
        for valores in dicionario.values():
            notas.append(valores)
    x = sum(notas)/len(notas)
    return x