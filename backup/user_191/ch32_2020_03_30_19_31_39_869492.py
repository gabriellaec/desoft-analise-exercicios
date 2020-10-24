def lista_primos(n):
    a=[]
    b=[]
    for i in range (1,n+1):
        if i==0 or i==1:
            b.append(i)
        elif i==2:
            a.append(i)
        else:
            divisores = 0
            for divisor in range(1, i):
                if i % divisor == 0:
                    divisores = divisores + 1
                    if divisores > 1:
                        break
            if divisores > 1:
                b.append(i)
            else:
                a.append(i)
    return(a)