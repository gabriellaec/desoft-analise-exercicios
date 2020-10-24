def lista_caracteres (palavra):
    i=0
    lista=[]
    while i < palavra:
        if not palavra in lista:
            lista.append(palavra)
            i+=1
    print (lista)