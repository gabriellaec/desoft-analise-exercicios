from math import sqrt
teste = {'atleta1':10,'atleta2':20,'atleta3':50}

def calcula_tempo(dicionario):
    tempos = {}
    for i in dicionario:
        tempos[i] = sqrt(200/dicionario[i])
    return tempos

nome = input("Nome do competidor: ")
aceleracao = float(input('Digite a aceleração do competidor: '))
data = {nome:aceleracao}
while nome != 'sair':
    nome = input("Nome de outro compertidor: ")
    if nome == 'sair':
        break
    aceleracao = float(input("Aceleracao de outro competidor: "))
    data[nome] = aceleracao

Tempos = calcula_tempo(data)

# Velho truque do "encontrar maior elemento da lista":
melhor_tempo = 1000000000
melhor_competidor = nome
for i in Tempos:
    if Tempos[i] < melhor_tempo:
        melhor_tempo = Tempos[i]
        melhor_competidor = i
print("O vencedor é {0} com tempo de conclusão de {1} s".format(melhor_competidor,melhor_tempo))