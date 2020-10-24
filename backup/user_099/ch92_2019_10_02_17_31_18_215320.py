def simplifica_dict(dicionario):
    lista=[]
    for chave in dicionario:
        lista.append(chave)
        lista.append(dicionario[chave])
    listando=[]
    listando.append(lista[0])
    for palavra in lista:
        for i in range(len(listando)):
            if i!=len(listando)-1:
                if palavra!=listando[i]:
                    continue
                else:
                    break
            else:
                if palavra!=listando[i]:
                    listando.append(palavra)
    return listando