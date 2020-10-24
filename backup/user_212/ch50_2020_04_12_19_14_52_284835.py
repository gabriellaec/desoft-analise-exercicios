def junta_nome_sobrenome (a,b):
    nomes=[] 
    i=0
    espaco=' '
    while i< len(a)-1:
        junto=[a[i] + espaco + b[i]]
        nomes.append(junto)
        i += 1
    return nomes 
    
    
    