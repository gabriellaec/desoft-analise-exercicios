def lista_primos(num):
    if < 1:
        return []
    primos =[2]
    j=1
    while len(primos) < n:
        for i in range(2,j):
            if (j % i) == 0:
                break
            if i == j-1:
                primos.append(j)
        j += 1
    return primos
