lista = [['janeiro', '1'], ['fevereiro', '2'], ['março', '3'], ['abril', '4'],
                ['maio', '5'], ['junho', '6'], ['julho', '7'], ['agosto', '8'],
                ['setembro', '9'], ['outubro', '10'], ['novembro', '11'], ['dezembro', '12']]
mes_selecionado = str(input('Digite o nome de um mês: '))

for mes_e_numero in lista:
    mes = mes_e_numero[0]
    if mes = mes_selecionado:
        numero = mes_e_numero[1]
        print('O número do mês de {} é {}'.format(mes_selecionado, numero))
