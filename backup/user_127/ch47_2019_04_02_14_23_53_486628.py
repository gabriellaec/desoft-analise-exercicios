lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
a = int(input('Número do mês?')
while a > 12: 
	a = int(input('Número do mês?')
i = 0
n = len(lista)
while i < n:
	if a == i + 1:
        print(lista[i])
    i += 1
