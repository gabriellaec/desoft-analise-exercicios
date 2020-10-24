def eh_primo(x):
    if x >= 2:
        for y in range( 2, x ):
            if not ( x % y ):
                return False
    else:
        return False

    return True

def primos_entre(a,b):
    qntd_primos = 0
    x = a
    while x <= a:
        if eh_primo(x):
            qntd_primos +=1
        x+=1
        
    return qntd_primos