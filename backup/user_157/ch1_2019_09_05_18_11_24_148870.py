def calcula_valor_devido(valor_emprestado, n_meses, taxa_de_juros):
    for(i = 1; i <= n_meses; i++):
        valor_emprestado = valor_emprestado * (taxa_de_juros)^i
  	return valor_emprestado