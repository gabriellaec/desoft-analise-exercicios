def calcula_media(lista):
    notas = []
    for dic in lista:
        for k in dic:
            notas.append(dic[k])
            
    media = sum(notas)/len(notas)
    return media
