meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input ('Digite o mes: ')
i = 0
while i < len(meses):
    if mes == meses[i]:
        print (i + 1)
    i += 1