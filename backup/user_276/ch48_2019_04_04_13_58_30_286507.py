a = input('Escolha o nome de um mês:   ')
ind = -1
i = 0
lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
while i < len(lista):
    ind += 1
    i += 1
    if a in lista:
        print(ind)
