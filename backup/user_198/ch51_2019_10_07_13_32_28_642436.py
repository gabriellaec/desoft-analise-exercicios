def estritamente_crescente(num):
    cresc=[]
    l=len(num)
    cresc.append(num[0])
    maior=num[0]
    aux=0
    for i in range(1,l):
        aux=num[i]
        if aux>maior:
            maior=aux
            cresc.append(aux)
    return cresc