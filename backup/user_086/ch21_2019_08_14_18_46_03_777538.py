#valor inicial = sem os 10% // valor final= com os 10%
def calcula_dez_porcento(valorinicial):
	valorfinal=valorinicial*1,1
	return valorfinal
valorinicial2=int(input('Qual o valor da conta do restaurante? '))
print('Valor da conta com 10%: R${0:.2f}'.format(calcula_dez_porcento(valorinicial2)))
