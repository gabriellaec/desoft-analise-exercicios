def verifica_quadrado_perfeito(x):
    
    i = 1
    n = x-i
    while n>0:
        n = x-i
        i+=2
        if x-i == 0:
            return True
        elif x-i < 0:
            return False