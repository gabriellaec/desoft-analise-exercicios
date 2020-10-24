# Verificando se um número é quadrado perfeito

def verifica_quadrado_perfeito(n):
    m = n        # m é a variável de verificação
    i = 2        # Parâmetro para valores a serem subtraidos
    while m >= 0:
        m = m - i
        i += 2
    if m**2 == n:
        return True
    else:
        return False

print(verifica_quadrado_perfeito(9))