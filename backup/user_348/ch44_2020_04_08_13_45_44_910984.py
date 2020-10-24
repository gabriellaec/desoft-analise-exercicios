lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input('nome do mês:')

i = 0
while i < len(lista):
    i = i + 1
    if mes == lista[i]:
        print(i)
    