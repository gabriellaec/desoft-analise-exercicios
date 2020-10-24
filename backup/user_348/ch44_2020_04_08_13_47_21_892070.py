lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input('nome do mês:')

i = 0
while i < len(lista):
    if mes == lista[i]:
        print(i+1)
    i = i + 1
    