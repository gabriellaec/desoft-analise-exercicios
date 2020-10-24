def lista_caracteres (palavra):
    i=0
    lista=[]
    for i in palavra:
        if not palavra in lista:
            lista.append(palavra)
    print (lista)