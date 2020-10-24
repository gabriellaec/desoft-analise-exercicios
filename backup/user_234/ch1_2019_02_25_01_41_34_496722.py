def calcula_valor_devido(valor_emprestado, n_meses, taxa_juros):
    if n_meses > 0:
    	vlr_dvd = valor_emprestado * n_meses * taxa_juros
    	return vlr_dvd