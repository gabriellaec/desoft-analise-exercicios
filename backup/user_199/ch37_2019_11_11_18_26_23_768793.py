def lista_primos(n):
    if n%2==0:
        print(2)
    
    i=3
    while i<n:
        if n%i==0:
            print(i)
        i+=2
    
    return i
print(lista_primos(8))