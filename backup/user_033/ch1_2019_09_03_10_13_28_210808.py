def calculo_valor_devido(ValorEmprestimo,NumeroMeses, TaxaJuros):
	ValorFinal = ValorEmprestimo*(1+TaxaJuros/100)**NumeroMeses
	return ValorFinal
