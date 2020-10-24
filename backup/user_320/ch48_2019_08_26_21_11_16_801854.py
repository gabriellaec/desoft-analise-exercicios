meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

mes = input('Digite um mes: ')
for i, v in enumerate(meses):
    if mes.title() == v:
        print(i + 1)