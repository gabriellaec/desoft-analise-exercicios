def calcula_valor_devido (valor_emprestado, número_de_meses, taxa_de_juros):
    montante= valor_emprestado*(1+taxa_de_juros)**número_de_meses
    return montante
a = int(input('digite o valor emprestado: '))
b= int(input('digite um número de meses: '))
c= float(input('digite um valor para a taxa de juros: '))
print(calcula_valor_devido(a,b,c))
