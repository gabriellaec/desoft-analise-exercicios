x = input(' qual mes ')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i = 0
while i < 12:
    if x == meses[i]:
        print (i+1)
    i += 1