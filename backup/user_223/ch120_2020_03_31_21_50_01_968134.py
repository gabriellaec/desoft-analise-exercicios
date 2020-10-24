import random
dinheiro = 100
while dinheiro > 0:
	print ("Você tem {} dinheiros". format(dinheiro))
	aposta = input("Insira sua aposta: ")
	aleatorio = random.randint(0,36)
	if aposta == 0:
		break
	else:
		n_ou_p = input("Você deseja apostar em número(n) ou paridade(p)? ")

	if n_ou_p == "n":
		num = input("Escolha um número entre 1 e 36: ")
	elif n_ou_p == "p":
		chute_ip = input("Escolha se par(p) ou se ímpar(i): ")
	else:
		print("Você não escolheu nem n nem p")
		break

	if 1 <= num < 36 and num == aleatorio:
		dinheiro += 35*aposta
	elif 1 <= num < 36 and num != aleatorio:
		dinheiro -= aposta
	else:
		print ("Amado?")
		break

	if (chute_ip == "p" and (aleatorio%2)) or (chute_ip == "i" and not aleatorio%2):
		dinheiro += aposta
	elif (chute_ip == "i" and not aleatorio%2) or (chute_ip == "i" and aleatorio%2):
		dinehiro -= aposta