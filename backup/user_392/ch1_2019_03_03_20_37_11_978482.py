def calcula_valor_devido(valoremprestado, numerodemeses, taxadejuros):
    y = valoremprestado (1+taxadejuros)**numerodemeses
    return y