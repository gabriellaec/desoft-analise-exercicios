import random
r1 = random.randint (0, 36)
dinheiro = 100
aposta = 1
while dinheiro > 0:
    r1 = random.randint (0, 36)
	print ('você tem R$ {0}'. format (dinheiro))
	aposta = float (input ('Quanto você quer apostar? '))
	n_ou_p = input ('Você quer apostar em um número (n) ou paridade(p)?')
	if n_ou_p == 'n':
		numero = int(input('Escolha um número entre 1 e 36:')
		if numero == r1:
			valor_final = dinheiro + (35 * aposta)
		else:
			valor_final = dinheiro - aposta
	else:
		paridade = input ('Escolha entre Par (p) ou Impar (i):')
		if paridade == 'p':
			r1 % 2 == 0
			valor_final = dinheiro + aposta
		elif paridade == 'i':
			r1 % 2 != 0
			valor_final = dinheiro + aposta
		else:
			valor_final = dinheiro - aposta
            
print (r1)
print ('você tem R$ {0}'. format (valor_final))