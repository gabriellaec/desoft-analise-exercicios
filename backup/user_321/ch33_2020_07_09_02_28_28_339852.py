def primos_entre (a,b):
    i = 3
    n = a
    contagem = 0
    while n <= b:
        if n == 2:
            contagem += 1
        elif n == 1 or n == 0:
            n +=1
            continue
        elif(n%2==0):
            n += 1
            continue
        else:
            while (i<n):
                if (n%i==0) and i == n:
                    contagem += 1
                    break
                else:
                    i = i+2
        n += 1
    return contagem

print(primos_entre(10,100))
    