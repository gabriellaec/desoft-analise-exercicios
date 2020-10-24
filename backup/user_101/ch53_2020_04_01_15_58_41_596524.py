def soma_impares(l):
    novaL = []
    i = 0
    while i < len(l):
        if l[i] % 2 == 1:
            novaL.append(l[i])
        i += 1
    return sum(novaL)