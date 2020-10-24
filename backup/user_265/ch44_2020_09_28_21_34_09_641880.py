pede = input('Digite um mes: ')
nome = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

i = 0
while i < 12:
    if pede == nome[i]:
        print(i+1)
    i += 1