def verifica_quadrado_perfeito (n):
    i=1
    while i <= n:
        n=n-i
        i = i + 1
    if n == 0:
        return True
    else:
        return False 
        