def inverte_dicionario(dicionario):
    dn={}
    ls=[]
    for n in dicionario.values:
        for f,m in dicionario.items:
            if n==m and n not in dn:
                dn[n]=ls.append(f)
    return dn
                
        
    