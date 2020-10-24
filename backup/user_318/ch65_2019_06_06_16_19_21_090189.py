def acha_bigramas(string):
    lista=[]
    i=1
    while i<len(string):
        a=string[i-1]+string[i]
        if a  not in lista:
            lista.append(a)
        i+=1
    return lista