nome_mes = input('Informe o mês:\n')
lista = ['janeiro', '1'], ['fevereiro', '2'], ['março', '3'], ['abril', '4'], ['maio', '5'], ['junho', '6'], ['julho', '7'], ['agosto', '8'], ['setembro', '9'], ['outubro', '10'], ['novembro', '11'], ['dezembro', '12']
for i in range(len(lista)):
    if lista[i][0] == nome_mes:
        print("{0}".format(lista[i][1]))