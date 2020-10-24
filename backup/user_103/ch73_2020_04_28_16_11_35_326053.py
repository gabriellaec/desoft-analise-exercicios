def remove_vogais(letras):
    lista=[]
    i=0
    while i < len(letras):
        if letras[i]!='a' and 'e' and 'i' and 'o' and 'u':
            lista.append(letras[i])
        else:
            i+=1
        return lista
               