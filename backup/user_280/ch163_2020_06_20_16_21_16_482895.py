def calcula_media(lista):
    i = 0
    while i < len(lista):
        notas = []
        for nota in lista[i].values():
            notas.append(nota)
        i+=1
    media = sum(notas)/len(notas)
    return media