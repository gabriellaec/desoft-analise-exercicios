def apaga_repetidos(frase):
    frasemai=frase.upper()
    lista=[]
    listamai=[]
    for ele in frasemai:
        if ele not in listamai:
            listamai.append(ele)
            a=listamai.index(ele)
            lista.append(frase[a])
        else:
            listamai.append("*")
            lista.append("*")
    return (''.join(lista))
