def lista_primos(n):
    if n < 1:
        return[]
    primos = [2]
    x=3
    while len(primos) < n:
        for i in range(2,x):
            if x % i == 0:
                break 
            if i == x-1:
                primos.append(x)
            x +=1
    return primos
