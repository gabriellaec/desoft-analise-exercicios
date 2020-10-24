def calcula_fibonacci(n):
    fibonacci = [1,1]
    i = 0
    
    while i < n - 2:
        a = fibonacci[i] + fibonacci[i+1]
        fibonacci.append(a)
        i += 1
    return fibonacci

        
            