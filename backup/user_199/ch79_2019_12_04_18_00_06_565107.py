
lista1=['sp','mg','rs']
lista2=['sao paulo','uberlandia','floripa']
def monta_dicionario(lista1,lista2):
    dic={}
    for k in lista1:
        for v in lista2:
            dic[k]=v
    return dic
        
print(monta_dicionario(lista1,lista2))