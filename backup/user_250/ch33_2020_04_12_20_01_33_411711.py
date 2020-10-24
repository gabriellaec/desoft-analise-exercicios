def primos_entre(a,b):
    primos = []
    while a < b:
        Primo = True
        if a == 0 or a ==1:
            Primo = False
        if a%2 == 0 and a != 2:
            Primo = False
        else:
            i = 3
            while i < a:
                if a%i == 0:
                    Primo = False
                i = i+2
        if Primo = True:
            primos.append(a)
        a = a+1
    return primos
                