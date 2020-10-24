def calcula_fibonacci(c):
    fibonacci = [0]*c
    fibonacci[0]=1
    fibonacci[1]=1
    w=2
    while w<c:
        fibonacci[w]= fibonacci[w-1]+ fibonacci[w-2]
        w+=1
    return fibonacci
        
    