def fibonacci ():
    fibonacci [i+2] = fibonacci [i+1] + fibonacci [i]
    return fibonacci
    

def calcula_fibonacci (n):
    lista = []
    i = 0
    while i < n:
        lista = fibonacci(n)
    
    return lista
        