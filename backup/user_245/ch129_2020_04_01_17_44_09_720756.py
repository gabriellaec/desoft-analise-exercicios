def verifica_quadrado_perfeito(n):
    contador = 0
    lista_impar = []
    lista_impar.append(1)
    while n > 0:
        n = n - lista_impar[contador]
        num_impar = lista_impar[contador] + 2
        lista_impar.append(num_impar)
        contador += 1
    if n == 0:
        return True
    else:
        return False