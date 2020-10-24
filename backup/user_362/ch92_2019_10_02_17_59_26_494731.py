def simplifica_dict(dicionario):
    lista=[]
    for i in dicionario:
        if i not in lista:
            lista.append(i)
    return lista
dicionario={"abobora","abacate","abacate"}
print (simplifica_dict(dicionario))