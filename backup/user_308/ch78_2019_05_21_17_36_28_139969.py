aceler={}
temperas={}
def calcula_tempo(acel):
    tempo={}
    for corredor,aceleracao in acel.items():
        vf=(2*aceleracao*100)**0.5
        t=vf/aceleracao
        tempo[corredor]=t
    return tempo

x=input("Nome do atleta: ")
y=0
while x!="sair" and y !="sair":
    y=int(input("Aceleração do atleta: "))
    if y!="sair":
        aceler[x]=y
        x=input("Nome do atleta: ")

maxt=0
corredorvencedor=0
for corredor,tempo in calcula_tempo(aceler).items():
    if tempo>maxt:
        maxt=tempo
        corredorvencedor=corredor
print("O vencedor é {0} com tempo de conclusão de {1:.2f}s".format(corredorvencedor,maxt))
