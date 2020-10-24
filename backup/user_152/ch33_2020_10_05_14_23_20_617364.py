def eh_primo (n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
         return True    
    elif n%2 == 0:
         return False
    else:
        x = 3
        while(x < n):
            if n % x == 0:
                break
            x = x + 2
        if x == n:
            return True
        else:
            return False

def primos_entre(a, b):
    primosn = []
    if b>a:
        lista = [0]*(b-a+1)
        i = 0
        while b>=a:
            lista[i] = a
            i += 1
            a += 1
        i = 0
        size = len(lista)
        while i<size:
            if eh_primo(lista[i]) == True:
                primosn.append(lista[i])
            i += 1

    return len(primosn)-1
