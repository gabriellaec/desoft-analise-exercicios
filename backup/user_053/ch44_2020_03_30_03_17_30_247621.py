lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

meses_do_ano = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

a=input('Digite o nome do mês: ')
i = 0
variavel = True

while variavel:
    if a == meses_do_ano[i]:
        print(lista[i])
        variavel = False
    else:
        i += 1