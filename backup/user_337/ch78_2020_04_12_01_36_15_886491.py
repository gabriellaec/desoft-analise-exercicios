nome = input('Nome?')
atletas = {}
while nome != 'sair':
    a = float(input('aceleração?'))
    atletas[nome] = a
    nome = input('Nome?')


valores = atletas.values()
dic = {}
for i in valores:
    tempo = (200/i)**(1/2)
    for k in atletas:
        if atletas[k] == i:
            dic[k] = tempo
key = dic.keys()
vence = key[0]
for e in key:
    if e < vence:
        vence = e
for q in atletas:
    if atletas[q] == e:
        atleta == q
print('O vencedor é {} com tempo de conclusão de {} s'.format(atleta, vence))
   

              
