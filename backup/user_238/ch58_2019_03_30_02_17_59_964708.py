def calcula_fibonacci(n):
    fibonacci=[1,1]
    fibonacci[0]=1
    fibonacci[1]=1
    i=2
    while i < n-1:
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
        i+=1
    return fibonacci
n=int(input('número '))
print(calcula_fibonacci(n))
        
    
    