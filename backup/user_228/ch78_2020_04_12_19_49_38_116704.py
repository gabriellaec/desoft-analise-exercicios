import math
def calcula_tempo(atletas):
    dic={}
    for n,a in atletas.items():
        t=math.sqrt(200/a)
        dic[n]=t
    return dic        
d={}
o=True
while o:
    nome=input("nome do bundao")
    if nome=="sair":
        o=False
    else:
        ac=int(input("aceleracao do bundao"))
        d[nome]=ac
vencedor=calcula_tempo(d)
print(f'O vencedor é {n} com tempo de conclusão de {t} s')




        
