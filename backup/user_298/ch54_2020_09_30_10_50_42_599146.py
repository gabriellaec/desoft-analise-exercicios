
def calcula_fibonacci(n):
    fibonacci = []
    fibonacci.append(1)
    fibonacci.append(1)
    t = 0
    while t < n:
        fibonacci_seguinte = fibonacci[t] + fibonacci[t+1]
        fibonacci.append(fibonacci_seguinte)
        t += 1
    return fibonacci[:n]