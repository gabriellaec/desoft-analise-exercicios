def estritamente_crescente(lista):
    for i in lista:
        i=0
        crescendo=[]
        print(lista[i])
        if lista[i+1]-lista[i]>0:
            crescendo.append(lista[i+1])
        return crescendo