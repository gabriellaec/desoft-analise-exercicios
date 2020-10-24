def calcula_tempo(dicionario1):
    dicionario2 = {}
    for i in dicionario1.keys():
        dicionario2[i] = ((200/dicionario1[i])**0.5)
    return dicionario2
exercicio = True
dicionario = {}
while exercicio:
    nome = input('Qual o nome do atleta? ')
    if nome != 'sair':
        aceleração = float(input('Qual o valor da acelerção? '))
        dicionario[nome] = aceleração
    else:
        break
o = calcula_tempo(dicionario)
b = min(o.values())
for u in o.keys():
    if o[u] == b:
        print('O vencedor é {0} com tempo de conclusão de {1} s'.format(u, o[u]))
        
        