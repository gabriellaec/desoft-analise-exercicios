def lista_primos(n):
    primos = []
    impar = 3
    if num % 2 == 0:
        if num!= 2:
            return False
        else:
            return True
    elif num == 1:
            return False
    else:
        while impar<num:
            if num%impar!=0:
                return False
            else:
                primos.append(num)
                impar+=2
                """
    if n ==1:
        return False
    for d in range(3,n):
        if d/
            primos.append(d)
    return primos"""