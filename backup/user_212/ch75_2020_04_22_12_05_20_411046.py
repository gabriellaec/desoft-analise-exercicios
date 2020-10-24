def eh_primo (n):
    if n == 2:
        return True 
    elif n == 0 or n == 1 or n < 0:
        return False 
    elif n%2 == 0:
        return False 
    else:
        contador = 3
        while contador < n:
            if n%contador == 0: 
                return False 
            contador +=2
        return True 



def verifica_primos(lista):
    dici={}
    for n in lista:
        dici[n]=eh_primo(n)
    return dici
        