def quantos_uns(n):
    i=0
    contador=0
    for e in n:
        if n[i:i+1]=='1':
            contador+=1
    i+=1
        
    return contador