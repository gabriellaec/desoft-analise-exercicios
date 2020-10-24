def estritamente_crescente(lista):
    listac=[]
    i=0
    c=0
    while i < len(lista):
        if i==0:
            listac.append(lista[i])
            c=lista[i]
        if lista[i] > c:
            listac.append(lista[i])
            c=lista[i]
        i+=1
    return listac
lista=[1,2,4,2,3,5,2,8,7,8,9,3,4]
print(estritamente_crescente(lista))