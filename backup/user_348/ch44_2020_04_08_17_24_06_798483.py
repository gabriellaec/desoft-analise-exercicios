#usando uma lista
lista = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
mes = input('nome do mês:')

i = 0
while i < len(lista):
    if mes == lista[i]:
        print(i+1)
    i = i + 1

#usando dicionário
mes = {'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4, 'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8, 'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12}
numero = input('digite o nome do mes: ')

    