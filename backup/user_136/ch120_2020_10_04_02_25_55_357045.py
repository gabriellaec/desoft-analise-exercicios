import random
controle= True
dinheiro= 100

while controle:
    print ('Você possui R${0:.2f} reais'.format(dinheiro))               #serve para dizer quanto de dinheiro vc tem
    s=random.randint(0, 36)                                        #sorteia os números
    print (s)
    if dinheiro<=0:                                                #serve para dizer que você perdeu caso o seu dinheiro entre seja menor ou igual a 0
        print ('você perdeu')
        controle= False
    else:
        aposta= float(input('Qual a aposta ?R$'))                         # o usuário diz o valor que quer apostar
        if aposta== 0:
            print ('fim de jogo')
            print ('você terminou com {0:.2f}'.format(dinheiro))
            controle= False
        else:
            if aposta>dinheiro:                                              # se o valor for maior do que ele possui ele recebe 'valor insuficiente' e manda repetir a aposta
                print ('valor insuficiente')
            else:                
                num_par_ou_imp= input('A aposta é em um número ou paridade? ') # pergunta se a aposta é par ou impar ou número
                if num_par_ou_imp== 'n':                                       # entra nessa condição se ele tivesse digitado
                    numero= float(input('Qual o número ? '))                         # o usuário diz o número que acha que vai ser
                    if num_par_ou_imp== 'n' and aposta>0:               #caso ele ponha 'n' ele vai entrar nessa condição
                        if numero==s:                                       
                            novo= aposta * 35                     # caso ele acerte ele entra nessa condição e o seu dinheiro é contabilizado e dito ao jogador
                            dinheiro= novo + dinheiro
                            print ('parabens você acertou')
                        elif numero!= s:                                       
                            dinheiro= dinheiro - aposta           # caso ele erre ele entra nessa condição e o seu dinheiro é descontado e dito ao jogador
                            print ('Que pena você errou')
                else:        
                    if num_par_ou_imp== 'p' and aposta>0:
                        if s%2== 0:
                            dinheiro= dinheiro + aposta
                            print ('parabens você acertou')
                        elif s%2!= 0:
                            dinheiro= dinheiro - aposta
                            print ('que pena você errou')
                    
                    elif num_par_ou_imp== 'i' and aposta>0:
                        if s%2== 0:
                            dinheiro= dinheiro - aposta
                            print ('que pena você errou')
                        elif s%2!= 0:
                            dinheiro= dinheiro + aposta
                            print ('parabens você acertou')