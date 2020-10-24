def calcula_fibonacci(n):
    fibonacci=[]
    contador=0
    while len(fibonacci)<n:
        if contador==0 or contador==1:
            fibonacci.append(1)
        else:
            fibonacci.append(fibonacci[contador-2] + fibonacci[contador-1])
        contador+=1
    return fibonacci