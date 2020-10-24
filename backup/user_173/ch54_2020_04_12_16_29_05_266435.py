def fibonacci ():
    fibonacci [i] = fibonacci [i-1] + fibonacci [i-2]
    return fibonacci
    

def calcula_fibonacci (n):
    lista = []
    i = 0
    while i < n:
        fibonacci [i] = fibonacci [i-1] + fibonacci [i-2]
        i += 1
    
    return lista
        