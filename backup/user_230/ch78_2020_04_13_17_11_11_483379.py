import math as m
atletas=dict()
while True:
    nome=input("Digite o nome do atleta ou sair:")
    if nome=="sair":
        break
    else:
        atletas[nome]=int(input("Valor da aceleração do atleta:"))  
for k,v in atletas.items():
    atletas[k]=m.sqrt(200/v)
tempo=list(atletas.values())
lista_atletas=list(atletas.keys())

print("O vencedor é {0} com tempo de conclusão de {1}s".format(lista_atletas[tempo.index(min(tempo))], min(tempo)))