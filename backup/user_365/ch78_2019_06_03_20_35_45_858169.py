nome=input("nome do corredor")
aceleracao=float(input("aceleração"))
dic={}
while nome!="sair":
    dic[nome]=aceleracao
    nome=input("nome do corredor")
    if nome == "sair":
        print(dic)
    else:
        aceleracao=float(input("aceleração"))
tempo=calcula_tempo(dic)
for nome,tempo in tempo.items():
    