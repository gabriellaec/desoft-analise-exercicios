import random

def main():
	dinheiro = 100
	while(dinheiro > 0):
		print(dinheiro)
		aposta = float(input("Qual sua aposta?\n"))
		if aposta == 0:
			break
		else:
			tipo_aposta = input("Você escolhe número ou paridade?\n")
			Sorteio = random.randint(0, 36)
			if tipo_aposta == "n":
				numero = int(input("Escolha um número entre 1 e 36\n"))
				if (numero == Sorteio):
					dinheiro = dinheiro + 35*aposta
				else:
					dinheiro = dinheiro - aposta
			elif (tipo_aposta == "p"):
				paridade = input("Par ou impar?\n")
				if Sorteio == 0:
					dinheiro = dinhero - aposta
				elif Sorteio%2 == 0 and paridade == "p":
					dinheiro = dinheiro + aposta
				elif Sorteio%2 == 1 and paridade == "i":
					dinheiro = dinheiro + aposta
				else:
					dinheiro = dinheiro - aposta  
			else:
				break
        

main()