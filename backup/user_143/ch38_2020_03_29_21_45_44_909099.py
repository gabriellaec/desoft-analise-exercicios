def quantos_uns(num):
    numero=str(num)
    i=0
    count=0
    b=len(numero)
    while i<b:
        if numero[i] == '1':
            count+=1
            i+=1
        else:
            i+=1
    return count
        