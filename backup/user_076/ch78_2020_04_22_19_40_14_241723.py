nome = input("Digite o nome do atleta ou escolha sair: ") 
nomes_aceleração = dict()

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

nomes_tempo = dict()
nomes_tempo = calcula_tempo(nomes_aceleração)

menor_tempo = 0
lista = []

for k,v in nomes_tempo.items():
    lista.append(v)

menor_tempo = min(lista)

for k,v in nomes_tempo.items():
    if v == menor_tempo:
        vencedor = k

print ("O vencedor é {0} com tempo de conclusão de {1} s".format(vencedor,menor_tempo))
