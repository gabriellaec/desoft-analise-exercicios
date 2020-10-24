def calcula_total_da_nota(valor_produto, quantidade):
    nota_fiscal = []
    soma = 0
    for i in range(len(valor_produto)):
        nota_fiscal.append(valor_produto[i]*quantidade[i])
        soma += nota_fiscal[i]
    return soma