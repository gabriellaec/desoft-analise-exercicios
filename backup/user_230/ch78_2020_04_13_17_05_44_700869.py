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
tempo=list(dicionario.values())
lista_atletas=list(dicionario.keys())
menor_t=min(tempo)
vencedor=tempo.index(min(tempo))

print("O vencedor é {0} com tempo de conclusão de {1}s".format(vencedor, menor_t))