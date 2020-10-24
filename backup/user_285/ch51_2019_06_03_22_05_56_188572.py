def estritamente_crescente(lista):
    lista_crescente=[]
    i=0
    while i <len(lista):
        if lista[i]<lista[i+1]:
            lista_crescente.append(lista[i])
        i+=1
    return lista_crescente

def estritamente_crescente(lista):
    lista_crescente=[]
    maior=0
    for i in range(len(lista)):
        if lista[i]>maior:
            lista[i]==maior
            lista_crescente.append(maior)
    return lista_crescente
        