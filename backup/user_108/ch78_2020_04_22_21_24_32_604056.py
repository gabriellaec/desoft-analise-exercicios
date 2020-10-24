def calcula_tempo(acels):
    return {nome : (200/acels[nome])**(1/2) for nome in acels}
sair = False
aceleracoes = {}
while not sair:
    nome = input()
    if nome == "sair":
        sair = True
    else:
        aceleracoes[nome] = input()
vencedor = max(aceleracoes, key =aceleracoes.get)
print(aceleracoes)
print('O vencedor é {} com tempo de conclusão de {} s'.format(vencedor,aceleracoes[vencedor]))
        
        