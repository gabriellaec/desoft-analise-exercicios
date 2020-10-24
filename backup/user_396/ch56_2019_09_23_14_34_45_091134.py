def  calcula_total_da_nota(valor, quant)
	i = 0
	soma = 0
    while i < len(valor):
        soma = (valor[i] * quant[i])
        i += 1
    return soma