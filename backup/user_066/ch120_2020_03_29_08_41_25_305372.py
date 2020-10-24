import random
dinheiros = 100
print(dinheiros)
while dinheiros!=0:
    aposta = input()
    if aposta==0:
        break
    tipo_aposta = input()
    if tipo_aposta == 'n':
        numero = input()
        numero_sorte = random.randint(1,36)
        if numero_sorte == numero:
            dinheiros += 35*aposta
        else:
            dinheiros -= aposta
	elif tipo_aposta == 'p':
        numero_sorte = random.randint(0,1)
        if numero_sorte == 0:
            numero_sorte = 'p'
        else:
            numero_sorte = 'i'
        tipo_aposta = input()
        if tipo_aposta == numero_sorte:
        	dinheiros += aposta
        else:
            dinheiros -= aposta