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


def primos_entre(inicio, fim):
    contador = 0
    x = inicio

    while x <= fim:
        if eh_primos(x):
            contador += 1
        x += 1
    return contador

print(primos_entre(3,7))

