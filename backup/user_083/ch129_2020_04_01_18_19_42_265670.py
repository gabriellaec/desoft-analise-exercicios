def verifica_quadrado_perfeito(n):
    c=1
    while n>=c:
        n=n-c
        c+=c+2
        if n==0:
            return True
        else:
            return False
