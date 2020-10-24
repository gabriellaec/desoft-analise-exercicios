crescente=[]
def estritamente_crescente(lista):
    maior=lista[0]
    i=0
    while i<len(lista):
        if lista[i]>maior:
            maior=lista[i]
            crescente.append (lista[i])
        i+=1
    return crescente