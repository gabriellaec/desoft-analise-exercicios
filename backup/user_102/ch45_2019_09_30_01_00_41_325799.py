def zera_negativo(x):
    i = 0
    while i < len(x):
        if x[i] < 0:
            x[i] = 0
            i += 1

print(x)