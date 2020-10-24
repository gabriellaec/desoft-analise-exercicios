def verifica_quadrado_perfeito (n):
    m=n
    indice=0
    y=[2]
    while m>0:
        y.append (y[indice] + 2)
        m=m-y[indice]
        indice = indice +1
    if m**2 == n:
        return True
    else:
        return False
    