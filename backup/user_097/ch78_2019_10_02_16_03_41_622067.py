import math

def calcula_tempo(dic_atletas):
    dic_tempo_atletas = {}
    for nome, aceleracao in dic_atletas.items(): #quando se usa o items(), o primeiro "nome" é a chave a segunda "aceleracao" é o valor
        dic_tempo_atletas[nome] = math.sqrt(200/aceleracao)

    return dic_tempo_atletas


dic_atletas_velocidades = {}

while(True):
    nome_atleta = input("Digite o nome do atleta: ")
    if (nome_atleta=="sair"):
        break
    velocidade_atleta = float(input("Digite a velocidade do atleta: "))
    dic_atletas_velocidades[nome_atleta] = velocidade_atleta

dic_atletas_tempo = calcula_tempo(dic_atletas_velocidades)

menor = list(dic_atletas_tempo.values())[0]

for tempo in dic_atletas_tempo.values():
     if (tempo < menor):
         menor = tempo

print(dic_atletas_tempo)
print(menor)


for nome, valor in dic_atletas_tempo.items():
    vencedor = ""
    if valor == menor:
        vencedor = nome

print("O vencedor é", vencedor, "com tempo de conclusão de", menor, "s")