def remove_vogais(palavra):
    lista=[]
    i=0
    tamanho=len(palavra)
    while i<len(palavra):
        if palavra[i]!="a"or "e" or "i" or "o" or "u":
            lista.append(palavra[i])
        i+=1
        return lista 
    