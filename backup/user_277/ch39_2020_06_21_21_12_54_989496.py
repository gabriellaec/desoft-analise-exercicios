contador = 0
n = 1000
k = 0
while n != 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
        
    n-=1
        
print(n)
    