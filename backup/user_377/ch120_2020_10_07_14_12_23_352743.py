import random
jogando = True
sorteado = random.randint(0, 36)
valor = 100
while jogando:
    print('Voce tem {0} dinheiros'.format(valor))
    if valor <=0:
        print('Voce perdeu')
        break
    aposta= int(input('Qual valor que voce aposta?')
    if aposta ==0 :
        break
    pergunta= input('A aposta é em mumero ou paridade? (n/p)')
    if pergunta == 'n':
        pergunta2= int(input('Digite um numero de 1 a 36')
        if sorteado == pergunta2:
            valor = valor + aposta*35
        else:
            valor = valor - aposta
    elif pergunta == 'p':
        pergunta3= input('Par ou Impar?(p/i)') 
        if (pergunta3 == 'p' and sorteado % 2 == 0) or (pergunta 3 == 'i' and sorteado % 2 != 0):
            valor = valor + aposta
        else:
            valor = valor - aposta               
    sorteado = random.randint(0, 36)                       
                       
                