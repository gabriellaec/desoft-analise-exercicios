import math as m 
dic = {}
while True:
    resp = input('Qual o nome do atleta?: ')
    if resp == 'sair':
        break
    else:
        dic[resp] = input('Qual a acelereção do atleta?: ')


for k,v in dic.items():
    dic[k] = m.sqrt(200/int(v))

t = list(dic.values())
atletas = list(dic.keys())

print('O vencedor é {1} com tempo de conclusão de {0} s'.format(min(t),atletas[t.index(min(t))]))

