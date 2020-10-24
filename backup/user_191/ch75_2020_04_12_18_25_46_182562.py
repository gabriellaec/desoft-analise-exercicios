def verifica_primos(n):
    dic = {}
    for i in range(len(n)):
        if n[i]<=0:
            dic[n[i]]=('False')
        elif n[i]==1:
            dic[n[i]]=('False')
        elif n[i]==2:
            dic[n[i]]=('True')
        else:
            divisores = 0
            for divisor in range(1, n[i]):
                if i % divisor == 0:
                    divisores = divisores + 1
            if divisores > 1:
                dic[n[i]]=('False')
            else:
                dic[n[i]]=('True')
