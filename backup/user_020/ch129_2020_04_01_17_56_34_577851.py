lista_subtracao = []
lista_subtracao.append(1)
i = 0
def verifica_quadrado_perfeito(n):
    global i
    i += 1
    while n < i:
        impar_subtrai = lista_subtracao[i] + 2
        lista_subtracao.append(impar_subtrai)
        n -= lista_subtracao[i]
        if n == 0:
            return True
        elif n < 0:
            return False