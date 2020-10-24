from random import randint
dinheiro = 100
numero = randint (0, 36)
while dinheiro > 0:
    print('Você tem R${:.2f} para apostar!}').format(dinheiro)
    aposta = input('Qual o valor da aposta?')
    if aposta != 0:
        tipo = input('Qual o tipo da aposta?')
        if tipo == 'n':
            n = int(input('Digite um número de 1 a 36: ')
            if n = numero:
                print('Você ganhou!')
            	dinheiro += 35*aposta
            else:
            	print('Você perdeu!)
            	dinheiro = dinheiro - aposta
        if tipo == 'p':
        	paridade = str(input('Qual o tipo de paridade de sua aposta? ')
            if paridade == 'p':
            	i=0
                if n = i + 2:
                	dinheiro += aposta
                    print('Você ganhou!')
                else:
                	dinheiro -= aposta
                    print('Você perdeu!')
             elif paridade == 'i':
             	i=1
                if n = i + 2
                	dinheiro += aposta
                    print('Você ganhou!')
                else:
                	dinheiro -= aposta
                    print('Você perdeu!')
        
                                

                	           
            	
            
                
            