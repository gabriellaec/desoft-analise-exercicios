mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def numero_mes(numero, mes):
    numero_e_mes={}
    for i in range (len(mes)):
        numero_e_mes[numero[i]] = mes[i]
    return numero_e_mes

numero_input = input("Insira o numero do mês: ")
if numero_input in numero_mes(numero, mes):
    mes = numero_mes(numero, mes)[numero_input]
    print("O mes de número {} é {}".format(num_input, mes))
else:
    print("Não existe esse mês")