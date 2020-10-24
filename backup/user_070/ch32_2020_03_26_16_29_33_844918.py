def lista_primos(n):
    elemento=2
    divisor=3
    lista=[0]*n
    indice=0
    while n>indice:
        lista[indice]=elemento
        elemento+=1
        indice+=1
        if elemento%2==0:
            while elemento%2==0 or (elemento%divisor==0 and elemento>divisor):
                divisor=3
                elemento+=1
                while elemento%divisor!=0:
                    divisor+=2
    return lista