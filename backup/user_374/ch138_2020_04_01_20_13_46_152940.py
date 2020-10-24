perg1 = input('Código está executando? ')
verdade = True
teste = True
while teste:
    verdade = True
    if perg1 == 'n':
            print('Corrija o código e tente de novo')
            perg1 = input('Código está executando? ')
       
    elif perg1 == 's':
        while verdade:
                perg2 = input('o código Produz o resultado correto? ')
                if perg2 == 'n':
                            print('Corrija o código e tente de novo e volte para o começo de tudo')
                            verdade = False
                            perg1 = input('Código está executando? ')
                            break
                elif perg2 == 's':
                            print('Parabéns!')
                            teste = False 
                            verdade = False
                            
        