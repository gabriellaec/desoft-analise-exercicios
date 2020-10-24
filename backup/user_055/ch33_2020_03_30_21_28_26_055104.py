def primos_entre(a,b):
    lista = []
    if a <= 2:
        lista.append(2)
    if b == 1:
        lista.pop(0)
    lista_ab = [a]
    primo = a
    while lista_ab[-1] <= b:
        i = 1
        while i < primo:
            i += 1
            if primo % i == 0:
                break
            if i == (primo - 1) and a <= primo <= b:
                lista.append(primo)
        primo += 1
        lista_ab[-1] += 1
    return len(lista)