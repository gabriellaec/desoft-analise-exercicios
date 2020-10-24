def verifica_quadrado_perfeito(n):
    i=1
    y=1
    while n>=i:
        y=n-i
        if y==0:
            return True
        else:
            return False
        i+=2
print(verifica_quadrado_perfeito(25))