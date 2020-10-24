def acha_bigramas(string):
    lista = []
    lista2 = []
    
    for i in range(0,len(string)):
        lista.append(string[i:i+2])
        
    for i in lista:
        if len(i) >= 2:
            lista2.append(i)
           
    return lista2