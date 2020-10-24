def calcula_valor_devido(c,i,n):
    valor= c*((1+i)**n)
    return valor
#m=montante;n=tempo em meses;i=taxa de juros compostos;c= capital aplicado
print(calcula_valor_devido(500,0.5,6))