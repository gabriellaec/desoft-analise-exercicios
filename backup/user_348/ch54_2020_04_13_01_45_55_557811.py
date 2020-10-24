def calcula_fibonacci(n):
    if n ==1:
        fibonacci = [1]
    else:  
        fibonacci = [1,1]
        i = 2
        while i < n:
            numero = fibonacci[i-1] + fibonacci[i-2]
            fibonacci.append(numero)
            i = i + 1
        return fibonacci
        