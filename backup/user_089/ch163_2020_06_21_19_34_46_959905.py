def calcula_media(lista):
    notas = []
    for e in lista:
        for v in e.values():
            notas.append(v)
    numero = len(notas)
    notas = sum(notas)
    return notas/numero