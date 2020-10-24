def f(n):
    if n%2 == 0:
        n = n/e
    else:
        n = 3*n +1
    return n
y = True
i = 0
contador = 1000

for i in range(0, contador, 1):
    n = i
    print(n)
    while(y and n != 1):
        n = f(n)
        if n != 1:
            i += 1
        else:
            y = False
        print(i)