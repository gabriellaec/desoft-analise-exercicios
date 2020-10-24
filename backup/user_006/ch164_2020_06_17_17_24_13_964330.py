def traduz(lista, dicio):
    final=[]
    for i in lista:
        for e in dicio.keys():
            if i==e:
                port=dicio[e]
                final.append(port)
    return final
    