numeromax = 0  
sequencia = 0

def Collatz(n):
    i = 1
    while n>1:
        if n%2 == 0:
            n = n/2
            i+=1
        else:
            n = 3*n+1
            i+=1
        if n == 1:
            return i

for p in range(1000,1,-1):
    n = Collatz(p)
    if n > sequencia:
        numeromax = p
        sequencia = n
print(numeromax)