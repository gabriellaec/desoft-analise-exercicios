def calcula_valor_devido(c,i,t):
    Valor_Devido = c*(1+i)**t
    return Valor_Devido

c= float(input('Valor_Emprestado: '))
i= float(input('Taxa_de_Juros: '))
t= float(input('Número_de_Meses: '))

print (calcula_valor_devido(c,i,t))