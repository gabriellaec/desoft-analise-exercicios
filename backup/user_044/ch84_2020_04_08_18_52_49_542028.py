def inverte_dicionario(dicionario):
    dn={}
    ls=[]
    for n in dicionario.values:
        if n not in dn:
            for f,m in dicionario.items:
                if n==m:
                    dn[n]=ls.append(f)
    return dn
                
        
    