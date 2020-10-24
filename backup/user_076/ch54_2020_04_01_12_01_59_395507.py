def calcula_fibonacci(n):
    contador = 2
    fibonacci = []
    fibonacci [0] == 1
    fibonacci [1] == 1
    while contador < n:
        fibonacci [contador] = fibonacci [contador-1] +fibonacci [contador-2]
        contador +=1
    return fibonacci
        