def acha_bigramas(string):
    lista=[]
    cont = 0
    while cont < len(string)-1:
        if not string[cont:cont+2] in lista:
        	lista.append(string[cont:cont+2])
        cont+=1
    return lista