import random
dinheiro = 100
while dinheiro > 0:
	print ("Você tem {} dinheiros". format(dinheiro))
	aposta = float(input("Insira sua aposta: "))
	aleatorio = random.randint(0,36)
	if aposta <= 0 or aposta > dinheiro:
		break
	else:
		n_ou_p = input("Você deseja apostar em número(n) ou paridade(p)? ")

	if n_ou_p == "n":
		num = int(input("Escolha um número entre 1 e 36: ")) #até aqui ta funcionando. A partir daqui ele vai pro ultimo if
		if n_ou_p == "n" and 1 <= num <= 36 and num == aleatorio:
			dinheiro += 35*aposta
			print (dinheiro)
		elif n_ou_p == "n" and 1 <= num <= 36 and num != aleatorio:
			dinheiro -= aposta
			print (dinheiro)
		else:
			print ("Nova rodada!")

	elif n_ou_p == "p":
		chute_ip = input("Escolha se é par(p) ou se é ímpar(i): ")
		if n_ou_p == "p" and ((chute_ip == "p" and (aleatorio%2)) or (chute_ip == "i" and not aleatorio%2)):
			dinheiro += aposta
			print (dinheiro)
		elif n_ou_p == "p" and ((chute_ip == "p" and not aleatorio%2) or (chute_ip == "i" and aleatorio%2)):
			dinheiro -= aposta
			print (dinheiro)
		else:
			print("Nova rodada!")

	else:
		print("Você não escolheu nem n nem p!")
		break