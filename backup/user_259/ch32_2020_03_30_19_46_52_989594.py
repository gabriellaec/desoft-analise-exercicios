def lista_primos(n):
    primos = []
    nao_primos= []
    i=0
    while len(primos)<n:
        if i==0 or i==1:
            nao_primos.append(i)
            i+=1
        elif i==2:
            primos.append(i)
            i+=1
        else:
            divisores = 0
            for divisor in range(1, i):
                if i % divisor == 0:
                    divisores = divisores + 1
                    if divisores > 1:
                        break
            if divisores > 1:
                nao_primos.append(i)
                i+=1
            else:
                primos.append(i)
                i+=1
    return primos
