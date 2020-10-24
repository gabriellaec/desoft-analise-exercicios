def verifica_quadrado_perfeito(n):
    i=1
    while n>=i:
        if n-i==0:
            return True
        elif n==4:
            return True
        else:
            return False
        i+=i+2
