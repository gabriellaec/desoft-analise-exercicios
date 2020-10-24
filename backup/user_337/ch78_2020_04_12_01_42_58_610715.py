nome = input('Nome?')
atletas = {}
i = 0
while nome != 'sair':
    a = float(input('aceleração?'))
    atletas[nome] = a
    nome = input('Nome?')
    if i == 0:
        vence = a
    i+= 1

valores = atletas.values()
dic = {}
for i in valores:
    tempo = (200/i)**(1/2)
    for k in atletas:
        if atletas[k] == i:
            dic[k] = tempo
valor = dic.values()
for e in valor:
    if e < vence:
        vence = e
for q in atletas:
    if atletas[q] == e:
        atleta = q