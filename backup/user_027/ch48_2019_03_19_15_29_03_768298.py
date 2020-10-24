mes = input('Diga o nome do mês: ')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
cont = 1
while mes != meses[cont-1]:
    cont += 1
print(cont)