def estritamente_crescente(lista):
    lista_crescente=[]
    maior=lista[0]
    for i in range(len(lista)):
        if lista[i]>maior:
            lista[i]==maior
            lista_crescente.append(maior)
    return lista_crescente
        
        