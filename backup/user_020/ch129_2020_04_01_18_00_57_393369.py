
def verifica_quadrado_perfeito(n):
    lista_subtracao = []
    lista_subtracao.append(1)
    i = 0
    while n > 0:
        impar_subtrai = lista_subtracao[i] + 2
        lista_subtracao.append(impar_subtrai)
        n -= lista_subtracao[i]
        i += 1
        if n == 0:
            return True
        elif n < 0:
            return False
print(verifica_quadrado_perfeito(1))