import random
dinheiro = 100
jogo = True
while dinheiro > 0 and jogo == True :
    print('Você tem R${:.2f} para apostar!'.format(dinheiro))
    aposta = int(input('Qual o valor da aposta?'))
    if aposta != 0:
        tipo = input('Qual o tipo da aposta?')
        numero = random.randint(0, 36)
        if tipo == 'n':
            valor = int(input('Digite um número de 1 a 36: '))
            if valor == numero:
                print('Você ganhou!')
                dinheiro += 35*aposta
            else:
            	print('Você perdeu!')
            	dinheiro -= aposta
        if tipo == 'p':
            paridade = input('Qual o tipo de paridade de sua aposta? ')
            if numero%2 == 0:
                resultado = 'p'
            else:
                resultado = 'i'
            if valor == resultado:
                dinheiro += aposta
                print('Você ganhou!')
            else:
                dinheiro -= aposta
                print('Você perdeu!')
    else: 
        jogo == False           
print('Impossível realizar o jogo')
                
            