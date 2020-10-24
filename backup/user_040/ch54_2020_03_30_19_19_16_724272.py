Fibonacci = []*n
Fibonacci.append(1)
Fibonacci.append(1)
x=2
def calcula_Fibonacci(n):
    while x<n:
        Fibonacci[x] = Fibonacci[x-1] + Fibonacci[x-2]
        x+=1