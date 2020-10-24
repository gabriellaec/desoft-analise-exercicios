def remove_vogais(palavra):
    vogais=["a","e","i","o","u"]
    i=0
    lista=list(palavra)
    while(i<len(lista)):
        if(lista[i] in vogais):
            lista.remove(lista[i])
        i+=1
    return str.lower(" ".join(lista))