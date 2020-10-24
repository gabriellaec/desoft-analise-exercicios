x = input('Nome do mês: ')
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
i = 0
while i<12:
    if x == meses[i]:
        print(i+1)
    i += 1