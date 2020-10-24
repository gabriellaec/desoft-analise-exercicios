import random
dinheiro = 100
while dinheiro > 0:	
	print ("Você tem {} dinheiros". format(dinheiro))
	aposta = float(input("Insira sua aposta: "))
	sorteado = random.randint(0,36)
	if aposta <= 0 or aposta > dinheiro:
		break
	else:
		n_ou_p = input("Você deseja apostar em número(n) ou paridade(p)? ")

	if n_ou_p == "n":
		num = int(input("Escolha um número entre 1 e 36: "))
		if num == sorteado:
			dinheiro += 35*aposta
			print (dinheiro)
			print (sorteado)
		else:
			dinheiro -= aposta
			print (dinheiro)
			print (sorteado)

	elif n_ou_p == "p":
		chute_ip = input("Escolha se é par(p) ou se é ímpar(i): ")
		if (chute_ip == "p" and sorteado%2) or (chute_ip == "i" and not sorteado%2):
			dinheiro += aposta
			print (dinheiro)
			print (sorteado)
		else:
			dinheiro -= aposta
			print (dinheiro)
			print (sorteado)
	else:
		print("Você não escolheu nem n nem p!")
		break