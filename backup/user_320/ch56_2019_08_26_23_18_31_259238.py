def calcula_total_da_nota(a,b):
    nota = list(zip(a, b))
    soma = 0
    for elemento in nota:
        soma += elemento[0] * elemento[1]
    return soma