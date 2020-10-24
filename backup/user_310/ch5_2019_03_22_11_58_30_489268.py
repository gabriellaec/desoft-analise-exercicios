def maior_primo_menor_que(n):
    numero=n
    i=2
    if numero==0 or numero==1:
        return False
    while i<numero:
        if numero%i==0:
            numero-=1
        i+=1
    return True