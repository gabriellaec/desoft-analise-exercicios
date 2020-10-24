def numero_de_termos(x):
    n = 0
    while 0 < n < 1000:
        if n % 2 ==0:
            n = n/2
            x +=1
        elif n == 1:
            return x
        else:
            n = 3*n + 1
            x +=1
    return n 