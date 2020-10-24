def remove_vogais(word):
    lista_1=''
    i= 0
    while i<len(word):
        if word[i] not in ['a', 'e', 'i', 'o', 'u']:
            lista_1 += word[i]
        i+=1
    return lista_1
    
            
        