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

variavel_tempo = 0
lista = []

for nomes in atletas.keys():
    if variavel_tempo > atletas[nomes]:
        lista.append(atletas[nome]) #tempo
        lista.append(nomes) #nome
        variavel_tempo = atletas[nome]
print('O vencedor é {0} com tempo de conclusão de {1} s'.format(lista[len(lista)], lista[len(lista)-1]))
    