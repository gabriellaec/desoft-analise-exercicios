def verifica_quadrado_perfeito(x):
    i = 1
    n = x-i
    i+=2
    while n>0:
        if x-i == 0:
            return True
        elif x-i < 0:
            return False