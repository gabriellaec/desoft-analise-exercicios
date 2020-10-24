def conta_bigramas (string):
    i=0
    lista=[]
    dic={}
    while i<(len(string)-1):
        soma= string[i] + string[i+1]
        lista.append(soma)
        if lista[i] in dic:
            values = string.count(lista[i])
            dic[lista[i]] = values
        else:
            dic[lista[i]] = 1
        i+=1

    return dic 
            
    