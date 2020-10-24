contador = 0
n = 1000
k = 0
while n != 1:
    if n % 2 == 0:
        k = n/2
    else:
        k = 3 * n + 1
        
    n-=1
    print(k)
print(k)
    