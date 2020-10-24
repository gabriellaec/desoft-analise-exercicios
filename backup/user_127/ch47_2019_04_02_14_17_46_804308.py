lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
a = int(input('Número do mês?')
i = 0
n = len(lista)
while i < n:
	if a == i:
        print(lista[i - 1])
    i += 1