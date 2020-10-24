deposito=int(input('Qual o depósito inicial? '))
juros=int(input('Qual a taxa em porcentagem? '))

contador=1

while contador<25:
    
    montante=deposito*(1+juros/100)**contador
    contador+=1
    
    print ("Valor da mês é: R$ {0:.2f}".format(montante))
    
valor_ganho=montante-deposito
print ("Valor total ganho é: R$ {0:.2f}".format(valor_ganho))