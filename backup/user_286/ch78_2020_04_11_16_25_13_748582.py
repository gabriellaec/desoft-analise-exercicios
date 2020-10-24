dic_init = {}
nome = ''
while True:
    nome = input('Qual o nome do atleta? ')
    if nome == 'sair':
       break
    aceleracao = int(input('Qual a aceleracao dele? '))
    dic_init[nome] = aceleracao

def ace_temp(aceleracao):
    temp = (200/aceleracao)**(1/2)
    return temp

def calcula_tempo(dic):
    dic_tempo = {}
    for nome, aceleracao in dic.items():
        tempo = ace_temp(aceleracao)

        dic_tempo[nome] = tempo

    return dic_tempo

dic_tempo = calcula_tempo(dic_init)

for nome, tempo in dic_tempo.items():
    if tempo == min(dic_tempo.values()):
        print("O vencedor é {} com tempo de conclusão de {} s".format(nome, tempo))