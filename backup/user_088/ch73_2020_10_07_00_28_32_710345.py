def remove_vogais(palavra):
    vogais=["a","e","i","o","u"]
    i=0
    lista=list(palavra)
    lista2=[]
    while(i<len(lista)):
        if(lista[i] not in vogais):
            lista2.append(lista[i])
        i+=1
    return str.lower(' '.join(lista2))