def calcula_fibonacci(num):
    i = 2
    fibonacci = [ 1, 1]
    while i < num:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
        i += 1
    return fibonacci

        