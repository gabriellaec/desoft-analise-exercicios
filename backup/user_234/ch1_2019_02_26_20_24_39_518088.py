def calcula_valor_devido(valor_emprestado, n_meses, taxa_juros):
    	vlr_dvd = valor_emprestado * ((1 + taxa_juros)**n_meses)
    	return vlr_dvd

