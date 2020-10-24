def calcula_tempo(nada):
    dic = {}
    for atleta, aceleracao in nada.items():
        tempof = (200/aceleracao)**0.5
        dic[atleta] = tempof
    return dic

a = 0
compete = {}
while a != "sair":
    a = input("Digite o nome do atleta: ")
    b = input("Digite a aceleracao do atleta: ")
    compete[a] = b
    
atletatempos  = calcula_tempo(compete)
tempo = []
for i in atletatempos.values():
    tempo.append(i)
    
print('O vencedor é {} com tempo de conclusão de {} s'.format(atletatempos[max(tempo)], max(tempo)))