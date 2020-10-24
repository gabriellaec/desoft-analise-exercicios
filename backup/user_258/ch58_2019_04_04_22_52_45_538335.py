def calcula_fibonacci(n):
    fib=[]
    fib[0]=1
    fib[1]=1
    i=2
    while i<n:
    	fib[i]=fib[i-1]+fib[i-2]
        i+=1
    return fib
    
    