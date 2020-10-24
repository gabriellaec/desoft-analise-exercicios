def eh_primo(n):
    if n <=1:
        return False
    for e in range(2,n):
        if (n % e == 0):
      		  return False
    return True

def verifica_primos(lista):
    d={}
    for num in lista:
        status=eh_primo(num)
        if num not in d:
            d[num]=status
    return d
lista=[1,2,3,4,45,5,6,7,8]
print(verifica_primos(lista))

