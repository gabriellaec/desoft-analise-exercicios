def eh_primos (x):
    if x==1 or x==0 :
        return (False)
    if x==2:
        return (True)
    if x%2==0:
        return (False)
    a=3
    while a<x:
        if x%a==0:
            return (False)
        a = a + 1

    return (True)


def maior_primo_menor_que(n):
    x = n
    while x >= 0:
        if eh_primos(x):
            return x
        x -= 1
    return -1

print (maior_primo_menor_que(10))
