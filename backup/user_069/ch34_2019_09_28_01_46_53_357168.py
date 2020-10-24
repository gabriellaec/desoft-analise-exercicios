valor = float(input('Qual o valor do depósito? '))
juros = float(input('Qual a taxa de juros? '))
mes = []
i = 0
mes[0] = valor
while 24 >= mes[i]:
	mes[i] = mes[i - 1]*juros
print(mes) 
    