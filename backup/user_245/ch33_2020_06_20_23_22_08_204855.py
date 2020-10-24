def eh_primo(num):
    impar = 3
    if num % 2 == 0:
        if num!= 2:
            return False
        else:
            return True
    elif num == 1:
            return False
    else:
        while impar<num:
            if num%impar==0:
                return False
            else:
                impar+=2
        return True
def lista_primos(n):
    primos = []
    a = 0
    i = 0
    while n>a:
        if eh_primo(i) == True:
            primos.append(i)
            a += 1 
        i+=1
    return primos
def primos_entre(a,b):
    tam = len(lista_primos(b))
    return tam