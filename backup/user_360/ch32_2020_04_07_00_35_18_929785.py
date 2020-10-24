def lista_primos(n):
    if n<1:
        return []
    primos [2]
    numero = 1
    while len(primos)<n:
        for i in range(2, numero):
            if numero%1==0:
                break
            if i==numero-1:
                primos.append(numero)
        numero+=1
    return primos
           
    