def lista_caracteres (palavra):
    i=0
    lista=[]
    for i in range(len(palavra)):
        if palavra[i] not in lista:
            lista.append(palavra[i])
    print (lista)
    
    
