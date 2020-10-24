def interseccao_valores(dicionario1,dicionario2):
    lista=[]
    for e in dicionario1.values():
        for i in dicionario2.values():
            if e==i:
                lista.append(e)
        return lista
                