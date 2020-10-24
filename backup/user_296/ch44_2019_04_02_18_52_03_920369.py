def soma_valores(a):
    s = 0
    i = 0
    while i < len(a):
        s += a[i]
        i += 1
    return s
lista = [input()]
print(soma_valores(lista))  