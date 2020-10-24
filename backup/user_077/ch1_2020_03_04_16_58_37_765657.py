#Considerando o montante inicial como 50 reais e os juros como de 5%,temos:
def calcula_valor_devido(x):
    y=50*1.05**x
    return y
#vejamos os juros após 12 meses
a=12
b=calcula_valor_devido(a)
print(b)


