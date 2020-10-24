def verifica_primos(n):
    dic = {}
    if n==0:
        dic[0]=(1>2)
    elif n==1:
        dic[1]=(1>2)
    elif n==2:
        dic[2]=(1<2)
    else:
        divisores = 0
        for divisor in range(1, n):
            if n % divisor == 0:
                divisores = divisores + 1
        if divisores > 1:
            dic[divisor]=(1>2)
        else:
            dic[divisor]=(1<2)