'''Essa fução joga dois dasos e soma o valor dos resultados de cada um.
Em seguida, pergunta-se ao usuário dois numeros e devolve se os numeros escolhidos
são maiores, menores ou se estão entre a soma dos dados.
na sequencia, pergunta-se quantos chutes o usuário deseja comprar para tentar acertar o numero sorteado.
Caso ele acerte o numero dentro dos chutes, ele recebe o valor do saldo restante multiplicado por 5
caso contrário, os chutes acabem, ele apenas fica com o saldo restante. 
'''
import random
dinheiros = 10
dado1 = random.randint(1,10)
dado2 = random.randint(1,10)
soma_dados = dado1 + dado2
numero = int(input('Escolha um número entre 2 e 20: '))
numero2 = int(input('Escolha um numero maior ou igual ao anterior: '))
if soma_dados < numero:
    print('Soma menor')
elif soma_dados > numero2:
    print('Soma maior')
else:
    print('Soma no meio') 
print(dinheiros)
chutes = int(input('Quantos chutes deseja compra? '))
saldo = dinheiros - chutes
while dinheiros > 0:    
    numero = int(input('Escolha um número entre 2 e 20: '))
    numero2 = int(input('Escolha um numero maior ou igual ao anterior: '))
    if soma_dados < numero:
        print('Soma menor')
    elif soma_dados > numero2:
        print('Soma maior')
    else:
        print('Soma no meio')
    if soma_dados == numero or soma_dados == numero2:
        dinheiros += saldo *5
        print('Você terminou o jogo com {0} dinheiros'.format(dinheiros))
        break
    elif chutes == 0:
        break
print('Você terminou o jogo com {0} dinheiros'.format(dinheiros))