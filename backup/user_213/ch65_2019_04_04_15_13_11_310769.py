def acha_bigramas(palavra):
    bigramas=[]
    i=0
    while i<len(palavra):
        bi=palavra[i:(i+2)]
        if bi not in lista:
            lista.append(bi)
        i+=1
        