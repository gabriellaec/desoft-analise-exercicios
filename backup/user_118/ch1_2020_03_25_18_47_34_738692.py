def calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros):
    m=valor_emprestado(1+taxa_de_juros)**número_de_meses
    return m
a=float(input('Valor emprestado:'))
b=float(input('Número de meses:'))
c=float(input('Taxa de juros:'))
k=calcula_valor_devido(a,b,c)
print (k)