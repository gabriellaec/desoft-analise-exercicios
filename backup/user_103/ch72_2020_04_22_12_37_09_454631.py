def lista_caracteres (palavra):
    i=0
    lista=[]
    for i in palavra:
        if palavra not in lista:
            lista.append(palavra)
    print (lista)
    
    
