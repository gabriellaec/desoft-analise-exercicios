#import
import random

#inicialização
print('Você possui 100 reais.')
dinheiro=100
valor_aposta = int(input("Quantos reais você quer apostar? "))

#jogo
i= (valor_aposta != "0" or "zero" and dinheiro != 0)
i = True
while i:
    questao = input('A aposta será em número(n) ou paridade(p)? ')
    if questao == 'n':
        digite = input("Digite um número de 1 a 36: ")
        sorteio = random.randint(0,36)
        print('O número sorteado foi {0}'.format(sorteio))
        if sorteio == digite:
            dinheiro= 100+(valor_aposta*35)
            print=('Parabéns, você tem {0} reais agora'.format(dinheiro))
        else:
            dinheiro= 100-valor_aposta
            print('Você tem {0} reais agora'.format(dinheiro))
    else:
        escolha_par_impar=input('Escolha par(p) ou ímpar(i): ')
        sorteio2 = random.randint(0,36)
        print('O número sorteado foi: {0}'. format(sorteio2))
        if escolha_par_impar=='p':
            if sorteio2 % 2 ==0:
                dinheiro= 100+(valor_aposta*2)
                print('Parabéns, você tem {0} reais agora'.format(dinheiro))
            else:
                dinheiro= 100-(valor_aposta) 
                print(dinheiro) 
        elif escolha_par_impar=='i':  
            if sorteio2 % 2 !=0:
                dinheiro= 100+(valor_aposta*2)
                print('Parabéns, você tem {0} reais agora'.format(dinheiro))
            else:
                dinheiro= 100-(valor_aposta) 
                print(dinheiro)        
else:
    print('Você perdeu')