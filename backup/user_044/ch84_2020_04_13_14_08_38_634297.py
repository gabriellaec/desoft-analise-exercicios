def inverte_dicionario(dicionario):
    dn={}
    ls=[]
    for n in dicionario.values():
        ls=[]
        if n not in dn:
            for f,m in dicionario.items():
                if n==m:
                    ls.append(f)
            dn[n]=ls        
    return dn
                
        
    