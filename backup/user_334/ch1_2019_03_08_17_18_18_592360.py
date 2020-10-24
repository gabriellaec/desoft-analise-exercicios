def calcula_valor_devido (valor emprestado, número de meses, taxa de juros):
    montante= valor emprestado*(1+taxa de juros)**número de meses
    return montante
a = int(input('digite o valor emprestado: /n'))
print(calcula_valor_devido(a))
    
