meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
m = input('Qual o nome do mês:')
i = 0
while i in range(len(meses)):
    if m == meses[i]:
        print(i+1)
    else:
        i += 1