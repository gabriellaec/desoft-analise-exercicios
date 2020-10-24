import math as m
atletas=dict()
while True:
    nome=input("Digite o nome do atleta ou sair:")
    if nome=="sair":
        break
    else:
        atletas[nome]=int(input("Valor da aceleração do atleta:"))  
def calcula_tempo(atletas):
    dicionario=dict()
    for i in atletas:
        dicionario[i]=m.sqrt(200/atletas[i])
    return dicionario
tempo=list(atletas.values())
lista_atletas=list(atletas.keys())

print("O vencedor é {0} com tempo de conclusão de {1}s".format(atletas[tempo.index(min(tempo))], min(tempo))