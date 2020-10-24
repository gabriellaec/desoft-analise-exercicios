def calcula_fibonacci(n):
    listafinal = []
    ant = 1 
    prox = 1
    for i in range (n+1):
        i = prox
        ant+=prox
        listafinal.append(ant)        
    return listafinal
 