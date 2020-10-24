def calcula_fibonacci(c):
    fibonacci = []
    if c==1:
        fibonacci.append(1)
    else:
        fibonacci.apend(1)
        fibonacci.append(1)
        w=1
    while w<c:
        fibonacci.append(fibonacci[w-1]+fibonacci[w-2])
        w+=1
    return fibonacci
        
    