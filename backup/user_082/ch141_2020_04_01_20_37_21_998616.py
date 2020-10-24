#O codigo ta funcionando direito, so aqui no servidor que esta dando tempo limite excedido.
#O jogo e suas mecanicas estao funcionando supimpa
import random
dinheiro=1000
jogo_continua=True
while jogo_continua:
    print('Voce tem {0} fichas.'.format(dinheiro))
    print('')
    pergunta_se_o_jogador_aposta = input('Voce quer apostar? ')
    print('')

    if pergunta_se_o_jogador_aposta == "não":
        jogo_continua=False
    
    if pergunta_se_o_jogador_aposta == "sim":
        dado_1=random.randint(1,6)
        dado_2=random.randint(1,6)
        soma= dado_1 + dado_2
        escolha_chute=True
        
        while escolha_chute:
            chute_jogador= input('Aposte 30 e chute o valor da soma dos dados: ')
            print('')

            if chute_jogador == soma:
                print('Voce ganhou 20 fichas')
                print('')
                dinheiro += 20
                escolha_chute=False
            
            elif chute_jogador != soma:
                dinheiro -= 30
                print('Voce perdeu 30 fichas')
                print('')
                pergunta_continuar= input('Quer continuar tentando ou vai desistir? Digite a soma ou desistir ')
                print('')
                    
                if pergunta_continuar == 'desistir':
                    escolha_chute=False
                    
                elif pergunta_continuar == soma:
                    print('Voce ganhou 50 fichas')
                    print('')
                    dinheiro +=50
                    escolha_chute=False
                    
                elif pergunta_continuar != soma:
                    print('Voce perdeu 20 fichas')
                    print('')
                    dinheiro -= 20
                    print('O valor de um dos dados foi de {0}.'.format(dado_1))
                    pergunta_continuar_denovo= input('Quer continuar tentando ou vai desistir? Digite Continuar ou desistir ')

                    if pergunta_continuar_denovo == 'desistir':
                        escolha_chute=False

                    elif pergunta_continuar_denovo == 'continuar':
                        dinheiro -= 10
                        chute_denovo= input('Qual o valor da soma? ')

                        if chute_denovo == soma:
                            print('Voce ganhou 50 fichas')
                            print('')
                            dinheiro +=50
                            escolha_chute=False
                            
                        elif chute_denovo != soma:
                            print('perdeu, tente novamente')
                            escolha_chute=False
