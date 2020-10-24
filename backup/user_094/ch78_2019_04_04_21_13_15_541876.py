import math
question = True
atletas = {}
while question:
    atleta = input("Dê o nome do atleta: ")
    if atleta != "sair":
        acel = float(input("Qual a aceleração do atleta? "))
        atletas[atleta]=acel
    else:
        question = False

def calcula_tempo(atletas):
    at_tempo = {}
    for k,v in atletas.items():
        tempo = (200/v)**0.5
        at_tempo[k]=tempo
    return at_tempo

menor = math.inf
nome = ''
at_tempo = calcula_tempo(atletas)
for k,v in at_tempo.items():
    if v<menor:
        menor = v
        nome = k
print("O vencedor é {0} com tempo de conclusão de {1} s". format(nome, at_tempo[nome]))
