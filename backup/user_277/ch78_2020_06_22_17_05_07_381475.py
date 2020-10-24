def calcula_tempo (atletas):
    tempo = {}
    for nome, a in atletas.items():
        t = (200/a)**(1/2)
        tempo[nome] = t
    return tempo

atletas = {}
i = True
while i:
    nome = input("digite um nome:")
    if nome != 'sair':
        aceleracao = int(input("digite a aceleração:"))
        atletas[nome] = aceleracao
    else:
        i = False

nomes_tempo = calcula_tempo(atletas)       

variavel_tempo = 10000000000
lista = []

for nomes in nomes_tempo.keys():
    if variavel_tempo > nomes_tempo[nomes]:
        lista.append(nomes_tempo[nomes]) #tempo
        lista.append(nomes) #nome
        variavel_tempo = nomes_tempo[nomes]

print('O vencedor é {0} com tempo de conclusão de {1} s'.format(lista[len(lista)-1], lista[len(lista)-2]))