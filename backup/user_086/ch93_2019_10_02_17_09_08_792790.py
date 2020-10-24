def verifica_numero(numero):
    numero=str(numero)
    i=0
    numeronovo=0
    while i<len(numero):
        num=int(numero[i])
        numeronovo+=num**num
        i+=1
    numero=int(numero)
    if numeronovo==numero:
        return True
    elif numeronovo<1:
        return False
    else:
        return False