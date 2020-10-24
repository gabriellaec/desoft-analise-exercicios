def verifica_quadrado_perfeito(numero_verificado):
    numero_impar = 1
    while numero_verificado > 0:
        numero_verificado -= numero_impar
        numero_impar += 2
    if numero_verificado == 0:
        return True #número é quadrado perfeito
    else:
        return False