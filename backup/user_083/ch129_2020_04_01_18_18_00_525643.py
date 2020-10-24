def verifica_quadrado_perfeito(n):
    i=1
    while n>=i:
        i+=i+2
        n=n-i
        if n==0:
            return True
        else:
            return False
        i+=i+2
