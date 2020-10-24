import math
def calcula_tempo(dicionario):
    dic_tempo={}
    for k,v in dicionario.items():
        t= math.sqrt(200/v)
        dic_tempo[k]=t
    return dic_tempo
dic={}
while True:
    nome=input("nome:")
    if nome=='sair':
        break
    aceleracao=float(input("aceleração:"))
    dic.update(calcula_tempo({nome:aceleracao}))
maior=0
nomedomaior=""
for k,v in dic.items():
    if v>maior:
        maior=v
        nomedomaior=k
print('O vencedor é {} com tempo de conclusão de {} s'.format(nomedomaior,maior))
                     
    