import math

corredores = {}

x = input('Digite um nome : ')

while x != 'sair':
	y = float(input('Qual sua aceleração? '))
	corredores[x] = y
	x = input('Digite um nome : ')

def calcula_tempo(dicionario):
	tempo = {}
	for k,v in dicionario.items():
		Vf = math.sqrt(0**2 + 2*v*(100 - 0))
		t =  (Vf-0)/v
		tempo[k] = t
	vencedor = {}
	menor = 10000
	i = 0
	for n,te in tempo.items():
		if te < menor:
			menor = te
			ven = n
			i += 1
	vencedor[ven] = maior
	print('O vencedor é {} com tempo de conclusão de {} s'.format(ven,maior))

print(calcula_tempo(corredores))
