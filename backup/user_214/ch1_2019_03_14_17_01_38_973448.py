def calcula_valor_devido(val_emp, num_meses, tax_juros)
	y=val_emp*((1+tax_juros)**num_meses)
    return y
