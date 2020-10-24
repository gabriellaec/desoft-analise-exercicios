def quantos_uns(n):
    soma=0
    a=0
    numerostr=str(n)
    while a<len(numerostr):
        if numerostr[a]=='1':
            soma=soma+1
        a=a+1
    return soma