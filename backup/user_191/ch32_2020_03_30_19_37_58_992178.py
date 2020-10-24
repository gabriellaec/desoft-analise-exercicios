def lista_primos(n):
    a=[]
    b=[]
    i=0
    while len(a)<n:
        if i==0 or i==1:
            b.append(i)
            i+=1
        elif i==2:
            a.append(i)
            i+=1
        else:
            divisores = 0
            for divisor in range(1, i):
                if i % divisor == 0:
                    divisores = divisores + 1
                    if divisores > 1:
                        break
            if divisores > 1:
                b.append(i)
                i+=1
            else:
                a.append(i)
                i+=1
    print(a)