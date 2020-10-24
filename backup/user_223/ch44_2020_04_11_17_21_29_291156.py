mes = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
def mes_num(mes, num):
    dic={}
    i=0
    while i<len(mes):
        dic[mes[i]] = num[i]
        i+=1
    return dic

mes_input = input("Insira o nome do mês: ")
if mes_input in dic:
    numero = dic[mes_input]
    print("O número do mes de {} é {}".format(mes_input, numero))
else:
    print("Não existe esse mês")