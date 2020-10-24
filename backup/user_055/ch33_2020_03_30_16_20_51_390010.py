def primos_entre(a,b):
    lista = []
    if a <= 2:
        lista.append(2)
    i = 0
    while i < ((b + 1) - a) + 1 :
        n_primo = i
        for x in range(2,n_primo):
            if n_primo % x == 0:
                break
            if x == (n_primo - 1):
                lista.append(n_primo)
        i += 1
    return len(lista)