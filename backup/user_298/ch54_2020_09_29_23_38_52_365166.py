fibonacci = []
fibonacci.append(1)
fibonacci.append(1)
def calcula_fibonacci(n):
    t = 0
    while t < n:
        fibonacci_seguinte = fibonacci[t] + fibonacci[t+1]
        fibonacci.append(fibonacci_seguinte)
        t += 1
    return fibonacci[:n]