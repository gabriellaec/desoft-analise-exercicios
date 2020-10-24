def interseccao_valores(dicionario1,dicionario2):
    lista=[]
    elemento=0
    for k1,v1 in dicionario1.items():
        for k2,v2 in dicionario2.items():
            if v1==v2:
                elemento=v1
                lista.append(elemento)
    return lista