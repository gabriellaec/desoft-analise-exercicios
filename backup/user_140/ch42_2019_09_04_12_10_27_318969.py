def conta_a(numero):
    count=0
    numero=str(numero)
    for i in numero:
        if i=="1":
            count+=1
    return count