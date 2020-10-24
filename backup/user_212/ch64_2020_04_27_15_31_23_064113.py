def acha_bigramas (string):
    i=0
    lista=[]
    bi=0
    while i<len(string):
        bi = string[i:i+2]
        if bi not in lista:
            lista.append(bi)
        i+=1
    