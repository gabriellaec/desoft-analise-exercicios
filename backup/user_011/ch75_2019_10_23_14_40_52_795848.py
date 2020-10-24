def eh_primo(n):
    primo = True
    a = 2
    if n == 0 or n == 1:
        return False
    while a<n:
        if n%a == 0:
            return False
        a+=1        
    return True

def verifica_primos(lista):
    dic = {}
    for n in lista:
        dic[n]=primo(n)
    return dic