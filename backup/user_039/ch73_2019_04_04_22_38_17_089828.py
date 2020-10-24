def remove_vogais(palavra):
    i=0
    lista=[]
    while i<len(palavra):
        i+=1
        if palavra[i]!='a' or 'e'or 'i' or 'o' or 'u':
            lista.append(palavra[i])
    return lista
            
        