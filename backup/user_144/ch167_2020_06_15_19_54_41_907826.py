def total_do_semestre_por_bairro(empresa):
	novo = {}
	for bairro in empresa:
		novo[bairro] = 0
		for mes in empresa[bairro][6:]:
			novo[bairro] += mes
	return novo

def bairro_mais_custoso(dic):
    total = total_do_semestre_por_bairro(dic)
    maior = 0
    maior_bairro = ""
    for bairro in total:
        custo = total[bairro]
        if custo > maior:
            maior = custo
            maior_bairro = bairro
    return maior_bairro