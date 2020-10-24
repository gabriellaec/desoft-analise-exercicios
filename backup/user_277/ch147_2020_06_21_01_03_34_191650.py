def mais_frequente(lista1):
    dicionario={}
    lista = []
    for i in lista1:
        if not i in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
            
    for palavra in dicionario.keys():
        lista.append(dicionario[palavra])
        print(lista)
    return lista