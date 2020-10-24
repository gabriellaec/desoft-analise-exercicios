Fibonacci[0]=1
Fibonacci[1]=1
def calcula_fibonacci(n):
    i = 0
    while(i < n):
        Fibonacci[i+2]=Fibonacci[i+1]+Fibonacci[i]   
        i=i+1
