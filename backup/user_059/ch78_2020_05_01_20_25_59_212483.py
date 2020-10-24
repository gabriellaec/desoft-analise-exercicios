def calcula_tempo(d):
    l = list(d.keys())
    a = list(d.values())
    d1 = {}
    for i in range(len(d)):
        d1[l[i]] = (100/(a[i]/2))**(1/2)
    return d1

d78 = {}

while True:
    x = input('Qual o nome do atleta? ')
    if x == 'sair':
        break
    else:
        y = float(input('Qual a aceleração doa atleta?' ))
        d78[x] = y
        
df = calcula_tempo(d78)        

finalv = list(df.values())
finaln = list(df.keys())
i = finalv.index(min(finalv))

print (f'O vencedor é {finaln[i]} com tempo de conclusão de {finalv[i]} s')
