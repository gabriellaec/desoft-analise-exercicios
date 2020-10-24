def junta_nome_sobrenome (a,b):
    nomes=[] 
    i=0
    espaco=" "
    while i<= (len(a)-1):
        nomes.append(a[i] + espaco + b[i])
        i += 1
    return nomes 