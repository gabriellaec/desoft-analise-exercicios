def sequencia (n):
    termos = 1
    sequência = True
    i = n
    while sequência:
        if i == 1:
            sequência = False
        elif i %2 == 0:
            i = i / 2
            termos += 1
        elif i %2 != 0:
            i = 3 * i + 1
            termos += 1
    return termos


sequencia_mais_longa = 0
i = 1
n = 0
while i < 1000:
    if sequencia(i) > sequencia_mais_longa:
        sequencia_mais_longa = sequencia(i)
        n = i
        i += 1
    else:
        i += 1

print (n)