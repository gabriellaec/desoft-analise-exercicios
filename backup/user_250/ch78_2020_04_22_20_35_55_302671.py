def calculatempo(a):
    t = (200/a)**(1/2)
    return t

def calcula_tempo(dic):
    dic2 = {}
    for i in dic:
        dic2[i] = calculatempo(dic[i])
    return dic2

dict2 = {}
perguntar = True
while perguntar == True:
    nome = input("Nome: ")
    if nome != "sair":
        ac = float(input("Aceleração: "))
        dict2[nome] = ac
    else:
        perguntar = False

minimo = 0
atleta = ""
dict3 = calcula_tempo(dict2)
for i in dict3:
    if minimo == 0 or minimo > dict3[i]:
        minimo = dict3[i]
        atleta = i

print("O vencedor é {0} com tempo de conclusão de {1} s".format(atleta, minimo))