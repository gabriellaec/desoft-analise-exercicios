dicionario={}
def simplifica_dict(dicionario):
    lista1=[]
    for i in dicionario:
        if i not in lista1:
            lista1.append(i)
    return lista1