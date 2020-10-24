def emprestimo(valor, meses, juros):
	total = valor*((1+juros)**meses)
	return total