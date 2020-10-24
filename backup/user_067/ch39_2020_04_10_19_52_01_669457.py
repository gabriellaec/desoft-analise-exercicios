def f(n):
    if n%2 == 0:
        n = n/2
    else:
        n = 3*n +1
    return n
i = 0

for i in range(0, 1000, 1):
    n = i
    j = 0
    while(n > 1):
        n = f(n)
        j += 1
    print(j)
 
