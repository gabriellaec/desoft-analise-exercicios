def calcula_total_da_nota (nota1, nota2):
    soma = 0
    i = 0
    while i < len(nota1):
        soma += (nota1[i] * nota2[i])
        i += 1
    return soma