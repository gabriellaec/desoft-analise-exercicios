def calcula_fibonacci(n):
    Fibonacci = []
    x=2
    if n==1:
        Fibonacci.append(1)
    elif n==2:
        Fibonacci.append(1)
        Fibonacci.append(1)
    if n>2:
        Fibonacci.append(1)
        Fibonacci.append(1)
        while x<n:
            Fibonacci[x] = Fibonacci[x-1] + Fibonacci[x-2]
            x+=1
    else:
        return None