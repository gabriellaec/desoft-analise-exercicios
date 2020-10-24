def calcula_euler(x, n):
    expansao = 0
    i = 0
    j = 1
    fatorial = 1
    while i < n:
        while j <= i:
            if i == 0:
                fatorial = 1
                j +=1
            else:
                fatorial *= j
                j += 1
            
        termo = (x**i)/fatorial
        expansao += termo
        i += 1
    return expansao

print (calcula_euler(2, 7))