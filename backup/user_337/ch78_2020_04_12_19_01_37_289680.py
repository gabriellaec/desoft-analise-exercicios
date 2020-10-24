nome = input('Nome?')
atletas = {}
while nome != 'sair':
    aceleracao = float(input('Aceleracao?'))
    atletas[nome] = aceleracao
    nome = input('nome?')

def calcula_tempo(atletas):
    valores = atletas.values()
    dic = {}
    for i in valores:
        tempo = (200/i)**(1/2)
        for k in atletas:
            if atletas[k] == i:
                dic[k] = tempo
    return dic

dicionario = calcula_tempo(atletas)
a = 0
for i in dicionario.values():
    if a == 0:
        b = i
    if i<b:
        b = i
    a += 1
for k in dicionario:
    if dicionario[k] == i:
        atl = k
print('O vencedor é {} com tempo de conclusão de {}s'.format(atl, i))
    
