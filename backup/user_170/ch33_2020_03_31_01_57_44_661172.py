
def primos_entre(a, b):
    primos = []
    while a <= b:
        ehPrimo = True
        if a == 0 or a == 1:
            ehPrimo = False
        if a%2==0 and a!=2:
            ehPrimo = False
        else:
            i = 3
            while i < a:
                if a%i==0:
                    ehPrimo = False
                i += 2
        if ehPrimo == True:
            primos.append(a)
        a += 1
    return len(primos)