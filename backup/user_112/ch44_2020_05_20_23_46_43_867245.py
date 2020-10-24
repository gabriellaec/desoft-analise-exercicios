nome = True
base = [0, 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

while nome:
    mes = input('nome do mês? ')
    print(base.index(mes))