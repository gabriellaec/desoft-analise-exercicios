n = 1000
calcula = 0
num = 0

def calcula_colatz(n):
    quantidade = 1
    while n!=1:
        if n%2==0:
            n = n/2
            quantidade+=1
        else:
            n = 3*n+1
            quantidade+=1
        
    return(quantidade)
    
while n != 1:
    if calcula_colatz(n) > calcula:
        calcula = calcula_colatz(n)
        num = n
    n-=1