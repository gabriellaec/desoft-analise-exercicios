def funcao(a, b):
for i in range(a, b):
	if i != primo:
		i = primo % i
		if i == 0:
			print ('Nap e primo')
			break
	else:
		print ('Primo')
		break
print ('Fim')
