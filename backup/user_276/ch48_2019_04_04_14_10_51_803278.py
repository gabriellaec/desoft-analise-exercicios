nome = input('Nome de um mês:   ')
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
i = 0
while i < len(meses):
    if meses[i] == nome:
        print(i+1)
    i += 1