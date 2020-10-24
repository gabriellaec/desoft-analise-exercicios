
def primos_entre(a, b):
    primos = []
    t = 0
    while a <= len(primos) <= b:
        ehPrimo = True
        if t == 0 or t == 1:
            ehPrimo = False
        if t%2==0 and t!=2:
            ehPrimo = False
        else:
            i = 3
            while i < t:
                if t%i==0:
                    ehPrimo = False
                i += 2
        if ehPrimo == True:
            primos.append(t)
        t += 1
    return len(primos)
