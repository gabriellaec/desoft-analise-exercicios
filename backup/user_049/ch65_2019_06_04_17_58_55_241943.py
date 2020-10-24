def acha_bigramas(string):
    lista=[]
    cont = 0
    while cont < len(string) - 3:
        lista.append(string[cont:cont+2])
        cont+=1
    return lista