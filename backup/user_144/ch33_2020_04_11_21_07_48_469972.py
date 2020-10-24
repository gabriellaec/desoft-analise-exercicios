    
def eh_primo(num):
    contador = 0
    for i in range(1, num + 1):
        if num % i == 0:
            contador += 1
    if contador == 2:
        return True
    else:
        return False

def primos_entre(a,b):
    qntd_primos = 0
    x = a
    while x <= a:
        if eh_primo(x):
            qntd_primos +=1
        x+=1
        
    return qntd_primos