def f(n):
    if n%2 == 0:
        n = n/2
    elif n%2 != 0:
        n = 3*n + 1
    return n

maior = 0
for i in range (0,1000,1):
    n = 1
    j = 1
    while n>1:
        n = f(n)
        j += 1
    if j>maior:
        maior = j
        num = i
        
print (num)        
        
    