#Jogo roleta simplificado
import random
print('Game On')
sorteado = random.randint(0,36)

#Valores de partida
dinheiro = 100
diminuição_dinheiro = 0
v = 0
p = 0

aposta = int(input('Aposte uma quantia:'))
print ('Dinheiro disponivel: {0}'.format(dinheiro))

#Regras do jogo
while diminuição_dinheiro < dinheiro:
    if  aposta == 0:
        break
    faça_aposta = input('Você quer apostar em um número (digite n) ou uma paridade (digide p para par ou i para impar)?')

    # Se jogador escolher chutar um número
    if faça_aposta == 'n':
        qual_numero = input('Digite um número de 1 a 36:')
        if qual_numero == sorteado:
            v = dinheiro + (aposta *35)
            print('Você ganhou mais {0}, agora você tem {1}'.format(aposta,v))
        else:
            p = dinheiro - aposta 
            print('Você perdeu {0}, agora você tem {1}'.format(aposta,p))

    #Se jogador escolher chutar que o número é par
    if faça_aposta == 'p':
        if sorteado % 2 == 0:
            v  = dinheiro + aposta
            print('Você ganhou {0}, agora você tem {1}'.format(aposta,v))
        else: 
            p = dinheiro - aposta
            print('Você perdeu {0}, agora você tem {1}'.format(aposta,p))

    # Se jogador escolher chutar que o número é impar
    if faça_aposta == 'i':
        if sorteado % 2 != 0:
            v  = dinheiro + aposta
            print('Você ganhou {0}, agora você tem {1}'.format(aposta,v))
        else: 
            p = dinheiro - aposta
            print('Você perdeu {0}, agora você tem {1}'.format(aposta,p))

    #Perguntar novamente uma aposta, para um loop
    dinheiro = dinheiro + v
    diminuição_dinheiro = diminuição_dinheiro + p
    aposta = int(input('Aposte uma quantia:'))
    print ('Dinheiro disponivel: {0}'.format(dinheiro))

print('End Game')