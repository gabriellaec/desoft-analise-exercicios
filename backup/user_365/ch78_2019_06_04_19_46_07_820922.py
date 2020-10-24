def calcula_tempo(dic):
    c={}
    for nome,acel in dic.items():
        c[nome]=(200/acel)**0.5
    return c

nome=input("nome do corredor")
aceleracao=float(input("aceleração"))
dic={}
d=1
while d>0:
    dic[nome]=aceleracao
    nome=input("nome do corredor")
    if nome == "sair":
        break
    else:
        aceleracao=float(input("aceleração"))
tempo=calcula_tempo(dic)
menor = min(tempo.values())
for nome,tempo in tempo.items():
    if tempo == menor:
        menor_nome=nome
print("O vencedor é {0} com tempo de conclusão de {1} s").format(menor_nome,menor)