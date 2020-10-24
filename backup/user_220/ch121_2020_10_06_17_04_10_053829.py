

def subtracao_de_listas(lista1,lista2):
    novalista=[]
    i=0
    while i < len(lista1):
        if lista1[i] in lista2:
            novalista.append(lista1[i])
            i+=1
        else:
            i+=1
    return novalista
