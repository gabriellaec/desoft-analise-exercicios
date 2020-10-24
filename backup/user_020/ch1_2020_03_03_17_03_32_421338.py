# Programa que calcula o valor devido após um período de tempo
def calcula_valor_devido(v,n,t):
    m = v*(1+t)**n
    return m
print(calcula_valor_devido(1000,10,5))