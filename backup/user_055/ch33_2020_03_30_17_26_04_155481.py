def primos_entre(a,b):
    lista = []
    if a <= 2:
        lista.append(2)
    for n_primo in range(a, (b + 1)):
        for x in range(2,n_primo):
            if n_primo % x == 0:
                break
            else:
                if x == (n_primo - 1):
                    lista.append(n_primo)
        n_primo += 1
    return len(lista)