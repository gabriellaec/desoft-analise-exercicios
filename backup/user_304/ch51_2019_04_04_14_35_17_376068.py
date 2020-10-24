def estritamente_crescente(lista):
    crescente=[]
    if lista!=[]:
        maior=lista[0]
        crescente.append(maior)
    i=0
    while i<len(lista):
        if lista[i]>maior:
            maior=lista[i]
            crescente.append (maior)
        i+=1
    return crescente