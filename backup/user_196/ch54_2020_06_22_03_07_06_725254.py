def calcula_fibonacci(n):
    listafinal = []
    ant = 1 
    prox = 1
    for i in range (n+1):
        i = prox
        soma = (ant += prox)
        listafinal.append(soma)
 