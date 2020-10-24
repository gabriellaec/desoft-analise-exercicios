def eh_primo(n):
    impar = 3
    if n <= 1:
        return False
    if n%2 == 0:
        if n == 2:
            return True
        else: 
            return False
    else:
        while impar < n:
            if n % impar == 0:
                 return False
            else:
                impar += 2
        return True
def lista_primos(n):
    primos = []
    i = 0
    while num >= len(primos):
        if eh_primo(i) == True:
            primos.append(num)
        i+=1
        return primos
