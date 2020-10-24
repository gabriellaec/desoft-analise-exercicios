def fatorial(n):
    resultado = 1
    numeros = 1
    while numeros <= n:
        resultado *= numeros
        numeros +=1 
        print(resultado)
    return resultado