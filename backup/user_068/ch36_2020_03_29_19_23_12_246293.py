def fatorial(n):
    resultado = 1
    numeros = 1
    while n >= 1:
        resultado *= numeros
        numeros +=1 
        print(resultado)
    return resultado