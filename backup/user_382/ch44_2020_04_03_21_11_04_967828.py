mes_lista = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho','Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
mes = input('Insira o nome do mes')

for i in mes_lista:
    if mes == i:
        print(mes_lista.index(i) + 1)