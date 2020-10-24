mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def mes_numero(mes, numero):
    mes_e_numero={}
    for i in range (len(mes)):
        mes_e_numero[mes[i]] = numero[i]
    return mes_e_numero

mes_input = input("Insira o nome de um mês: ")
if mes_input in mes_numero(mes, numero):
    numero = mes_numero(mes, numero)[mes_input]
    print("O mes de número {} é {}".format(mes_input, numero))
else:
    print("Não existe esse mês")