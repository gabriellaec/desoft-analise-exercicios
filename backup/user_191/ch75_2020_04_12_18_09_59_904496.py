def verifica_primos(n):
    dic = {}
    for i in range(n):
        if n[i]==0:
            dic[0]=(1>2)
        elif n[i]==1:
            dic[1]=(1>2)
        elif n[i]==2:
            dic[2]=(1<2)
        else:
            divisores = 0
            for divisor in range(1, i):
                if i % divisor == 0:
                    divisores = divisores + 1
            if divisores > 1:
                dic[divisor]=(1>2)
            else:
                dic[divisor]=(1<2)