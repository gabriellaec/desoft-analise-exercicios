def monta_dicionario(l1,l2):
    dicio = {}
    i = 0
    while i < len(l1):
        chave = l1[i]
        valor = l2[i]
        dicio[chave]=valor     
        i+=1
        
    return dicio
