def acha_bigramas (string):
    i=0
    lista=[]
    while i<len(string):
        bi = strnig[i:i+2]
        if bi not in lista:
            lista.append(bi)
        i+=1
    