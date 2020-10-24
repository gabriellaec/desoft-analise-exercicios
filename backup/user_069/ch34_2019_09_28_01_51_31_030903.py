valor = float(input('Qual o valor do depósito? '))
juros = float(input('Qual a taxa de juros? '))
mes = [valor]
i = 0
while 23 >= i:
	mes.append(mes[i - 1]*juros)
print(mes) 
    