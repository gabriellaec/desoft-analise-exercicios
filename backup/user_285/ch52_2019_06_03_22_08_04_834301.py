def eh_crescente(lista):
    lista_crescente=[]
    maior=0
    for i in range(len(lista)):
        if lista[i]>maior:
            maior=lista[i]
            lista_crescente.append(maior)
    if lista_crescente==lista:
        return True
    else:
        return False