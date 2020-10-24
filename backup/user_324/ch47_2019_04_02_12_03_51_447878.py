meses={"1": "janeiro", "2": "fevereiro", "3": "março", "4": "abril","5": "maio", "6": "junho", "7": "julho", "8": "agosto", "setembro": "9", "10": "outubro", "11": "novembro", "12": "dezembro"}
mes=input('Digite um número: ')
if mes in meses:
    print('Mes {0} é: {1}'.format(mes, meses[mes]))