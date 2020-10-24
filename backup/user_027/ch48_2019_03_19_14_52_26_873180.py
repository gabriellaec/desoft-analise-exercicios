mes = input('Diga o nome do mês: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
cont = 1
while mes != meses[cont-1]:
    cont += 1
print(cont)