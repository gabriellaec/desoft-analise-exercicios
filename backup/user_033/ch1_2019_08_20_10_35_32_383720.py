def calcula_valor_devido(ValorEmprestado, NumeroMeses, TaxaJuros):
    ValorFinal = ValorEmprestado*(1+TaxaJuros/100)**NumeroMeses
    return ValorFinal
