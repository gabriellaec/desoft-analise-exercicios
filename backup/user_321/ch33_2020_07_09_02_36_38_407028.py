def primos_entre (a,b):
    i = 3
    n = a
    contagem = 0
    while n <= b:
        if n == 2:
            contagem += 1
        else:
            while (i<n):
                if (n%i==0):
                    break
                else:
                    i = i+2
            contagem += 1
        n += 1
    print(contagem)
    return contagem
    