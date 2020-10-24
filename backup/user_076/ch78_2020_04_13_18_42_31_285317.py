nome = input("Digite o nome do atleta ou escolha sair: ") 
nomes_aceleração = dict()
nomes_tempo = dict()

while nome != 'sair':
    aceleração = float(input("Digite a aceleração do atleta: "))
    nomes_aceleração[nome] = aceleração
    nome = input("Digite o nome do atleta ou escolha sair: ")


def calcula_tempo(nomes_aceleração):
    nomes_tempo = dict()
    for i in nomes_aceleração:
        t = (200/nomes_aceleração[i])**(1/2)
        nomes_tempo[i] = t
    return nomes_tempo

nomes_tempo = calcula_tempo(nomes_aceleração)

#tempos = nomes_tempo.values

#i=0
#while i+1 < len(tempos):
    #if tempos[i]<tempos[i+1]:
        #vencedor = tempos[i]
    #i+=1

for i in nomes_tempo:
    for j in nomes_tempo:
        if nomes_tempo[i] > nomes_tempo[j]:
            vencedor == nomes_tempo[i]

print ("O vencedor é {0} com tempo de conclusão de {1} s".format(vencedor,i))

