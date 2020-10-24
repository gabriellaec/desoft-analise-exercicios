import math as m
def calcula_tempo(dic_atletas):
    dic={}
    for k,v in dic_atletas.items():
        t=m.sqrt(200/v)
        dic[k]=t
    return dic
ndic={}
b=True
while b:
    atleta=input("Insira o nome do atleta: ")
    if atleta == "sair":
        b=False
    else:
        ac=int(input("Insira a aceleração do atleta: "))
        ndic[atleta]=ac
tempo = cacula_tempo(ndic)
maximo = 10000000
vencedor = "ninguém"
if v<maximo:
    maximo = v 
    vencedor = k
print ("O vencedor é {} com o tempo de conclusão de {}s".format(vencedor, maximo))