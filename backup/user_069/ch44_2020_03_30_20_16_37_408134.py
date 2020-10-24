mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
n = input('Qual o nome do mês? ')
i = 0
while i < len(mes):
    if n == mes[i]:
        print(i+1)
    i += 1
