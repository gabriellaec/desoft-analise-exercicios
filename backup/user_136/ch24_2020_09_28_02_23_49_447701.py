def calcula_aumento(salario):
    if salario > 1250:
        aumento= salario * 0.1
        return 'Houve um aumento de {0:.2f}'. format(aumento)
    else: 
        aumento= salario * 0.15
        return 'Houve um aumento de {0:.2f}'. format(aumento)
w= int(input('qual o salário ? '))
print (calcula_aumento(w))