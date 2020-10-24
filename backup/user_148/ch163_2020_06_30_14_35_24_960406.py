def calcula_media(lista):
    notas = []
    for dic in lista:
        for k, v in dic.items():
            notas.append(v)

    return sum(notas)/len(notas)
