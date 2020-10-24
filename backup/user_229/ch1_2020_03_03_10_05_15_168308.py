def calcula_valor_devido(valoremprestado, númerodemeses, taxadejuros):
    y = valoremprestado*(1+taxadejuros)**númerodemeses
    return y
