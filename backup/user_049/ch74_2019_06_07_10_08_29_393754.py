def conta_bigramas(string):
    dicio={}
    lista=[]
    cont = 1
    o=0
    while cont < len(string):
        lista.append(string[o]+string[i])
        cont+=1
        o+=1

    for i in lista:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i]+=1
            
    return dict