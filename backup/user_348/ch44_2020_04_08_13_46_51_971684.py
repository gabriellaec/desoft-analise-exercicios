lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input('nome do mês:')

i = 1
while i < len(lista):
    if mes == lista[i]:
        print(i)
    i = i + 1
    