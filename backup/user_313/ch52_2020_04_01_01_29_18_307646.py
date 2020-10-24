def calcula_total_da_nota(l1,l2):
    a = len(l1)
    contador = 0
    NotaFiscal = [0]*a
    soma = 0

    while contador != a:
        NotaFiscal[contador]=l1[contador]*l2[contador]

        soma = soma + NotaFiscal[contador]
        contador = contador + 1
    return soma