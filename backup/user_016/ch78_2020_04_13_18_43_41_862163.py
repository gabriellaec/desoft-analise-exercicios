def calcula_tempo(dicionario1):
    dicionario2 = {}
    for i in dicionario1.keys():
        dicionario2[i] = ((200/dicionario1[i])**0.5)
    return dicionario2
exercicio = True
while exercicio:
    nome = input('Qual o nome do atleta? ')
    aceleração = float(input('Qual o valor da acelerção? '))
    if nome != 'sair':
        dicionario[nome] = aceleração
    else:
        calcula_tempo(dicionario)
        b = min(dicionario.values())
        for u in dicionario.keys():
            if dicionario[u] == b:
                print('O vencedor é {0} com tempo de conclusão de {1} s'.format(u, dicionario[u])
        
        