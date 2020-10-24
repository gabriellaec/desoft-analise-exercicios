d=float(input('deposito: '))
t=float(input('taxa: '))

contador = 1
deposito = 0
juros = 0

while contador<25:    
    montante = deposito*(1+juros/100)**contador
    contador += 1
    print ("Valor da mês é: R$ {0:.2f}".format(montante))
    
valor_ganho=montante-deposito
print ("Valor total ganho é: R$ {0:.2f}".format(valor_ganho))