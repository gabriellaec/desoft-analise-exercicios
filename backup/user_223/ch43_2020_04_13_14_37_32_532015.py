mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

def num_mes(num, mes):
    nummes={}
    for i in range (len(mes)):
        nummes[num[i]] = mes[i]
    return nummes

num_input = input("Insira o numero do mês: ")
if num_input in num_mes(num, mes):
    mes = num_mes(num, mes)[num_input]
    print("O mes de número {} é {}".format(num_input, mes))
else:
    print("Não existe esse mês")