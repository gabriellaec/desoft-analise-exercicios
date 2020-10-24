def calcula_media(lista):
    notas=0
    for i in range(len(lista)):
        notas+=lista[i][1]
    return notas/len(lista)