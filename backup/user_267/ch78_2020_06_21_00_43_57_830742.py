def calcula_tempo(dicio):
    nome_tempo = {}
    for e,a in dicio.items():
        t = (200/a)**(1/2)
        nome_tempo[e] = t
    return nome_tempo

nome_acel = {}
nome = input("Digite o nome: ")
while nome != "sair":
    aceleracao = int(input("Digite a aceleração: "))
    nome_acel[nome] = aceleracao
    nome = input("Digite o nome: ")

menor_tempo = float('inf')
chama_funcao = calcula_tempo(nome_acel)
for tempo in chama_funcao:
    if tempo < menor_tempo:
        menor_tempo = tempo

