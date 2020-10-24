def calcula_fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return[1]
    if n == 2:
        return[1,1]
    fibonacci = [1,1]
    
    for i in range(2,n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci
