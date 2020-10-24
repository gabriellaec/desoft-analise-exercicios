def calcula_valor_devido(valor,meses,juros):
    montante= valor*((1+juros)**meses)
    return montante

