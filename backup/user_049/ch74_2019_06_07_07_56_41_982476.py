def conta_bigramas(string):
    lista=[]
    cont = 0
    while cont < len(string)-1:
        if not string[cont:cont+2] in lista:
        	lista.append(string[cont:cont+2])
        cont+=1
    
    dict = {}
    indice = 0
    for i in lista:
        if not i in dict:
            dict[i] = indice
        indice+=1
    return dict