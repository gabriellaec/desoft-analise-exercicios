def quantos_uns(numero):
    texto=str(numero)
    i=0
    s=0
    while i<len(texto):
        if texto[i]=='1':
            s+=1
        i+=1
    return s

        