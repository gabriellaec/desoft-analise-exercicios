nome = True

while nome:
    mes = str.lower(input('nome do mês? '))
    base = [0, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
    print base.index(mes)