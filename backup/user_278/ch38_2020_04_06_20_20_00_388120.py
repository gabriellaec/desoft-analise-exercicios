def quantos_uns(a):
    numero = str (a)
    quantidade_1=0
    i=0
    while i < len(numero):
        if numero[i]=="1":
            quantidade_1 += 1
        i+=1
    return quantidade_1