nome = True

n = [0, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

while nome:
    mes = str.lower(input('nome do mês? '))
    for mes in n:
        print n.index(mes)