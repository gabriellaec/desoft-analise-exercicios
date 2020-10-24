
def lista_primos(n):
    i = 2
    if n <= 1:
        return False
    elif n == 2:
        return True
    while i < n:
       if n % i != 0:
        return True
    i += 1
    return True
   
print(lista_primos)