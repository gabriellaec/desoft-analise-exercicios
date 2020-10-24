def zera_valores(valores):
    
i = 0
while i < len(valores):
	if valores[i] < 0:
		valores[i] = 0
	i += 1
print(valores)