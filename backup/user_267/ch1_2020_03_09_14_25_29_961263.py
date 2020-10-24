def calcula_valor_devido(valoremprestado, taxadejuros, numerodemeses):
calcula_valor_devido = ( valoremprestado * ( 1 + taxadejuros)**numerodemeses)
print (calcula_valor_devido)