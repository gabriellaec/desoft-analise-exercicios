def calcula_valor_devido(valor_emprestado, n_meses, taxa_de_juros):
    for i in range(1, n_meses):
        valor_emprestado = valor_emprestado * (taxa_de_juros)^i
  	return valor_emprestado