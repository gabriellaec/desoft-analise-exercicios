def lista_primos(n):
    i=3
    while i<n:
        if n%i==0:
            print(i)
        i+=2
    return i
print(lista_primos(90))