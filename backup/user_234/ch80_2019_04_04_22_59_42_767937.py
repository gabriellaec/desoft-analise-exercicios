def interseccao_chaves(dic1,dic2):
    chaves=[]
    for chave in dic1 and dic2:
        if chave in dic1 and dic2:
            chaves.append(chave)
    return chaves