meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

mes = int(input('Digite um mes: '))
for i, v in enumerate(meses):
    if mes - 1 == i:
        print(v)