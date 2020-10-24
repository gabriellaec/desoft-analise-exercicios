def aniversariantes_de_setembro(dic):
    i=0
    nome=dic.keys()
    lista2=list(nome)
    data=dic.values()
    lista=list(data)
    b='09'
    while i <len(lista):
        c=lista[i][3:5]
        if c!=b:
            lista.pop(i)
            lista2.pop(i)
        else:
            i+=1
    dicionario=dict(zip(lista2, lista))
    return dicionario