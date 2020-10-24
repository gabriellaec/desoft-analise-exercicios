def lista_caracteres(stri):
    lista=[]
    i=0
    while i < len(stri):
        if stri[i] not in lista:
            lista.append(stri[i])
        i+=1
    return lista
stri='abacate'
q=lista_caracteres(stri)
print(q)