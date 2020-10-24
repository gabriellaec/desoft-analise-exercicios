def remove_vogais(palavra):
    i=0
    lista=[]
    while i<len(palavra):
        if palavra[i]!='a' and 'e'and 'i' and 'o' and 'u':
            lista.append(palavra[i])
        i+=1
    return lista
            
        