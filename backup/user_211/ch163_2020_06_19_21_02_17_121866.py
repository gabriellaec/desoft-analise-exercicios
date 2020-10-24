def calcula_media(lista):
    notas=[]
    for i in range(0,len(lista)):
        notas.append(lista[i].value)
    return sum(notas)/len(notas)