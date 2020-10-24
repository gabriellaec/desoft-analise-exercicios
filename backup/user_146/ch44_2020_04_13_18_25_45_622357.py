mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def mes_numero(mes, numero):
    mes_e_numero={}
    for i in range (len(mes)):
        mes_e_numero[mes[i]] = numero[i]
    return mes_e_numero

mes_input = input("Insira o nome de um mês: ')
if numero_input in numero_mes(numero, mes):
    mes = numero_mes(numero, mes)[numero_input]
    print("O mes de número {} é {}".format(numero_input, mes))
else:
    print("Não existe esse mês")