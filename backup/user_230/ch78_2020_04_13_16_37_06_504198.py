import math as m
atletas=dict()
while True:
    nome=input("Digite o nome do atleta ou sair:")
    acelera=input("Valor da aceleração do atleta:")
    if nome=="sair":
        break
    else:
        atletas[nome]=acelera
def calcula_tempo(atletas):
    dicionario=dict()
    for i in atletas:
        dicionario[i]=m.sqrt(200/atletas[i])
    for k in dicionario.items():
        if dicionario[k]==min(dicionario):
            vencedor==k
            tempo==dicionario[k]
    print("O vencedor é {0} com tempo de conclusão de {1}s".format(vencedor, tempo))