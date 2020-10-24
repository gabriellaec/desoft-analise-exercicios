def fatorial(n):
    fat= 1
    contador = 1
    while contador<= n:
        fat = fat*contador
        contador = contador + 1
    return fat
def calcula_euler(x,n):
    i = 1
    e = 1
    while i<n:
        e = e+(x**i)/fatorial(i)
        i = i+1
    return e
    

        