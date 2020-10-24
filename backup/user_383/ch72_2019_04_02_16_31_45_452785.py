def lista_caracteres(palavra):
    cont=0
    lista_letras=[]
    lista_letras.append(palavra[cont])
    while cont<len(palavra):
        if palavra[cont] not in lista_letras:
            lista_letras.append(palavra[cont])
        cont+=1
    return lista_letras
