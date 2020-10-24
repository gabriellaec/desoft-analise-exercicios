from random import randint
dinheiro = 100
while dinheiro > 0:
    print('Você tem R${:.2f} para apostar!}').format(dinheiro)
    aposta = input('Qual o valor da aposta?')
    if aposta > 0 and aposta <= 100:
        tipo = input('Qual o tipo da aposta?')
        numero = random(0, 36)
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
                caixa += aposta
                print('Você ganhou!')
            else:
                caixa -= aposta
                print('Você perdeu!')
    else: print('Tente outro valor')            
print('Impossível realizar o jogo')
                                

                	           
            	
            
                
            