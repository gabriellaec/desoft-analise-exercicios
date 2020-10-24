def interseccao_chaves(di1,di2):
    d1=di1.keys()
    d2=di2.keys()
    lista=[]
    for chave1 in d1:
        for chave2 in d2:
            if chave1==chave2:    
                lista.append(chave1)
    return lista