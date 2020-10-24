def conta_bigramas(string):
    contador={}
    lista=[]
    n=len(string)
    for i in range(0,n-1):
        if string[i]+string[i+1] not in lista:
            lista.append(string[i]+string[i+1])
            contador[string[i]+string[i+1]]=1
            i+=1
        elif string[i]+string[i+1] in lista:
            contador[string[i]+string[i+1]]+=1
            i+=1
    return contador