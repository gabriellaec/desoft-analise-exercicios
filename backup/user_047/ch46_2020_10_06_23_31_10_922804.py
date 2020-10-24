def numero_no_indice(x):
    lista=[]
    count = 0 
    while count<len(x):
        if count ==x[count]:
            lista.append(x[count])
        count +=1
    return lista