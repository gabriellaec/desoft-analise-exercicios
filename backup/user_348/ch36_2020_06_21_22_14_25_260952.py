#Com for
def fatorial (n):
    fat = 1
    for i in range(n):
        fat=fat*n
        n = n -1
    return fat

#Com while
def fatorial (n):
    # Define a fariável que calculará o fatorial com o seu valor inicial (1 pois independentemente do número n, multiplica por 1)
    fat = 1
    # Define a condição do loop
    while n > 1:
        # Calcula o fatorial
        fat = fat*n
        # Diminui o valor de n a cada loop
        n = n -1
    return fat

#Com for.2
def fatorial (n):
    fat = 1
    for i in range(1,n+1):
        fat=fat*i
    return fat