
def calcula_fibonacci(fibonacci):
    i = 2
    lista_fibonacci = []
    lista_fibonacci.append(fibonacci[0])
    lista_fibonacci.append(fibonacci[1])
    while i < len(fibonacci) :
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
        lista_fibonacci.append(fibonacci[i])
        i+=1
    return lista_fibonacci