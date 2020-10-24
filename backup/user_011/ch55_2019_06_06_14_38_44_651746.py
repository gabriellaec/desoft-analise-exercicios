def primos_entre(a,b):
    primos = []
    p = a
    i = 0
    while a <= p < b:
        p = a + i
        if p % 2 and p % 3 and p % 5 and p % 7 != int:
            primos.append(p)
        i += 1
            
    return primos