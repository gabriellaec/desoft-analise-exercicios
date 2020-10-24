import math
dicionario = {}
while True:
    pergunta = input ("Digite o nome do atleta ou sair: ")
    if pergunta == 'sair':
        break
    else:
        dicionario[pergunta] = int(input("Qual a aceleração do atleta?: "))

for nome,aceleracao in dicionario:
    dicionario[nome] = math.sqrt(200/dicionario[aceleracao])

t = list(dicionario.values())
atletas = list(dicionario.keys())
print("O vencedor é {1} com o tempo de conclusao de {0}s".format(min(t),atletas[t.index(min(t))]))
