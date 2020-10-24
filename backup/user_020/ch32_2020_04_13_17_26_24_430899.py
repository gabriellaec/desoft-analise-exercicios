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
def lista_primos(num):
    primos = []
    a = 0
    i = 0
    while num < a:
        if eh_primo(i) == True:
            primos.append(i)
            a+=1
            i+=1
        return primos
