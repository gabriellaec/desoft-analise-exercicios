def f(n):
    if n%2 == 0:
        n = n/e
    else:
        n = 3*n +1
    return n
y = True
i = 0

for i < 1000:
    n = i
    j = 0
    while(y and n != 1):
        n = f(n)
        if n != 1:
            j += 1
        else:
            y = False
        print(j)
        i += 1