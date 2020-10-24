nome = input('Digite o nome referente ao mês: ')
mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

i = 0

while i < len(mes):
    if nome == mes[i]:
        print(i+1)
    i += 1
    