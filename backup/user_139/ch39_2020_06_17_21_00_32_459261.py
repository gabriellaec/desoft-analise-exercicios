def sequencia (n):
    termos = 1
    sequência = True
    while sequência:
        if n == 1:
            sequência = False
        elif n %2 == 0:
            n = n / 2
            termos += 1
        elif n %2 != 0:
            n = 3 * n + 1
            termos +=1
    return termos

sequencia_mais_longa = 0
i = 0
while i < 1000:
    if sequencia(i) > sequencia_mais_longa:
        sequencia_mais_longa = i
        i += 1
    else:
        i += 1