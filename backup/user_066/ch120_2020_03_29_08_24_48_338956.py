import random
dinheiros = 100
print(dinheiros)
while dinheiros!=0:
    aposta = input()
    if aposta==0:
        break
    tipo_aposta = input()
    if tipo_aposta == 'número':
        numero = input()
        numero_sorte = random.randint(1,36)
        if numero_sorte == numero:
            dinheiros += 35*aposta
        else:
            dinheiros -= aposta
	else:
        parimpar = input()
        numero_sorte = random.randint(0,1)
        if numero_sorte == 1:
            numero_sorte = 'par'
        else:
            numero_sorte = 'impar'
        if parimpar == numero_sorte:
            dinheiros += aposta
		else:
            dinheiros -= aposta
            
        
    