def calcula_tempo(dicio):
    dicio2 = {}
    for i,j in dicio.items():
        dicio2[i] = (2*100/j)**.5
        
    return dicio2

dicio = {}
nome = ""
acel = 0

while nome != "sair":
    nome = input("Qual o nome do atleta? ")
    if nome != "sair":
        acel = int(input("Qual a sua aceleração?"))
        dicio[nome] = acel

tempo = calcula_tempo(dicio)

t=0
atlet = ""
for i,j in tempo.items():
    if j > t:
        t=j
        atlet = i
        
print("O vencedor é {0} com tempo de conclusão de {1} s".format(atlet,t))