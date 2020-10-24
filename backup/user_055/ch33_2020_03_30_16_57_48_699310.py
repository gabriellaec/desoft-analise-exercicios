def primos_entre(a,b):
    lista = []
    if a <= 2:
        lista.append(2)
    i = 0
    while i < ((b - a) + 1):
        n_primo = 3 + i 
        for x in range(2,n_primo):
            if n_primo % x == 0:
                break
            if x == (n_primo - 1):
                lista.append(n_primo)
        i += 2
    return len(lista)