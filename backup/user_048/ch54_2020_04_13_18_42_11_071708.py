def calcula_fibonacci(numero):
    if numero > 2:
        Fibonacci = [0]*numero
        Fibonacci[0] = 1
        Fibonacci[1] = 1

        i = 0
        while i < (numero- 2):
            Fibonacci[i+2] = Fibonacci[i+1] + Fibonacci[i]
            i += 1
        return Fibonacci
    elif numero== 2:
        Fibonacci = [1, 1]
        return Fibonacci
    else:
        Fibonacci = [1]
        return Fibonacci