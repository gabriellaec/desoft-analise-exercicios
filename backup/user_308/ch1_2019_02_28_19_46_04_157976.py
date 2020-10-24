def calcula_valor_devido(c,i,t):
    Valor_Devido = c*(1+i)**t
    return Valor_Devido

a= float(input('Valor_Emprestado: '))
b= float(input('Taxa_de_Juros: '))
c= float(input('Número_de_Meses: '))

print (calcula_valor_devido(a,b,c))