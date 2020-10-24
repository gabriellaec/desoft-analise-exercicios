import random 
dinheiro = 10000
chute3 = 0 

while True:
    print('Você terminou a partida com {0} dinheiros'.format(dinheiro))
    if dinheiro < 0:
        break
    resposta = input(('Você quer apostar?'))
    if resposta == 'não':
        break
    else:
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        soma_dados = d1 + d2
    
    while True:
        chute = input('Qual valor você gostaria de chutar?')
        dinheiro -=30
    
        if chute == soma_dados:
            dinheiro += 50
            break
        else:
            resposta2 = input('Você quer continuar apostando ou desistir?')
            if resposta2 == 'desistir':
                break
            else:
                chute2 = input('Chute novamente')
                dinheiro -= 20
        if chute2 == soma_dados:
            dinheiro += 50
            break
        else:
            print(d1)
            reposta3 = 'Você quer continuar apostando ou desistir?'
            if reposta3 == 'desistir':
                break
            if reposta3 == 'continuar':
                chute3 = input('Chute novamente')
                dinheiro -= 10
        if chute3 == soma_dados:
            dinheiro += 50
            break
        else:
            break

        
    
