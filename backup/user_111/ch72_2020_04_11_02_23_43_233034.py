def lista_caracteres(palavra):
    i=0
    lista_nova=[]
    while i<len(palavra):
        if palavra[i] not in lista_nova:
            lista_nova.append(palavra[i])
        i+=1
    return lista_nova