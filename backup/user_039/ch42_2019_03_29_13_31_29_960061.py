def quantos_uns(numero):
    numero=[]
    i=0
    s=0
    while i<len(numero):
        if numero[0][i]==1:
            s+=1
        i+=1
    return s
print(quantos_uns(x))
        