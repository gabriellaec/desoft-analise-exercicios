import random
dinheiro = 100
while dinheiro > 0:
	print (dinheiro)
	aposta = float (input ('Quanto você quer apostar? '))
    if aposta != 0:
		n_ou_p = input ('Você quer apostar em um número (n) ou paridade(p)?')
		if n_ou_p == 'n':
			numero = int(input('Escolha um número entre 1 e 36:')
            r1 = random.randint (0, 36)
			if numero == r1:
				dinheiro += 35 * aposta
                print (dinheiro)
			else:
				dinheiro -= aposta
                print (dinheiro)
		else:
			paridade = input ('Escolha entre Par (p) ou Impar (i):')
            r1 = random.randint (0, 36)
			if paridade == 'p':
				r1 % 2 == 0 or r1 == 0
				dinheiro += aposta
                print (dinheiro)
			elif paridade == 'i':
				r1 % 2 != 0
				dinheiro += aposta
                print (dinheiro)
			else:
				dinheiro -= aposta
                print (dinheiro)
	else:
		dinheiro == 0
            