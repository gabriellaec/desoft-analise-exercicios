def total_do_semestre_por_bairro(dicionario):
    
    dicionario2={}
    
    for i in dicionario:
        dicionario2[i]=0
        for e in dicionario[i]:
            dicionario2[i]+=e

    return dicionario2
    