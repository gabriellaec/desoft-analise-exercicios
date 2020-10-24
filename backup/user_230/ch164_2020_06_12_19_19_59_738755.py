def traduz (lista, dicio):
    nova_lista=[]
    for palavra in lista:
        if palavra in dicio:
            nova_lista.append(dicio[palavra])
    return nova_lista