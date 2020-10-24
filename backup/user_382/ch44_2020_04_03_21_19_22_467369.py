mes_lista = ['janeiro', 'fevereiro', 'março', 
             'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

mes = input('Insira o nome do mes')

for i in mes_lista:
    if mes == i:
        print(mes_lista.index(i) + 1)