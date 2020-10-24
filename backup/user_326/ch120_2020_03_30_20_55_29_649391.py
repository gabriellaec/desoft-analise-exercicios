import random


deseja_jogar = True
credit = 100
while deseja_jogar:
    random_number = random.randint(0,36)
    print("Você tem {} creditos".format(credit))
    valor_da_aposta = int(input('Você Aposta quanto? '))
    if valor_da_aposta == 0 or credit == 0:
        print('Thou hast fallen and lost thy life, unbeknownst to thee the name of the thief.  Thou hast lost thy wager and becomest but a cog of the strong')
        deseja_jogar = False
        break
    tipo_de_aposta = input('Sua aposta será em um número ou paridade? ')
    while tipo_de_aposta == 'n':
        aposta_n = int(input('Aposte um número: '))
        if aposta_n > 36 or aposta_n < 1:
            print('número inválido, por favor digite um número entre 1 e 36.')
            break
        elif aposta_n == random_number:
            print('Parabéns, você ganhou!')
            credit = credit + valor_da_aposta * 35
            break
        else:
            print('Você perdeu')
            credit = credit - valor_da_aposta
            break
    while tipo_de_aposta == 'p':
        aposta_p = input('Aposte par ou ímpar: ')
        elif random_number % 2 == 0 and aposta_p == 'p':
            print('Parabéns, você ganhou!')
            credit += valor_da_aposta
            break
        elif random_number % 2 != 0 and aposta_p == 'i':
            print('Parabéns, você ganhou!')
            credit += valor_da_aposta
            break
        else:
            print('Você perdeu')
            credit -= valor_da_aposta
            break