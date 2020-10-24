def calcula_fibonacci(n):
    Fibonacci = []
    x=2
    if n>2:
        Fibonacci.append(1)
        Fibonacci.append(1)
        while x<n:
            número = Fibonacci[x-1] + Fibonacci[x-2]
            Fibonacci.append(número)
            x+=1
        return Fibonacci
    elif n == 2:
        Fibonacci.append(1)
        Fibonacci.append(1)
        return Fibonacci
    elif n == 1:
        Fibonacci.append(1)
        return Fibonacci
    else return None