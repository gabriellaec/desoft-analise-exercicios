nome = True

while nome:
    mes = str.lower(input('nome do mês? '))
    n = [0, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    for mes in n:
        print n.index(mes)