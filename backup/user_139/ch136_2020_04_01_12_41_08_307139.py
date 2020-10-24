dado1 = random.randit (0,6)
dado2 = random.randit (0,6)
dado3 = random.randit (0,6)
soma = dado1 + dado2 + dado3
#fase de dicas:
print ('Você tem {0} dinheiros'.format(dinheiro))
if dinheiro == 0:
    print ('Você perdeu')
else:
    r1 = input ('Você quer uma dica?')
    if r1 == 'sim':
        dinheiro -= 1
        x = input('Fale um número: ')
        y = input('Fale um número: ')
        z = input('Fale um número: ')
        if x == soma or y == soma or z == soma:
            print ('Está entre os 3')
        else:
            print ('Não está entre os 3')
    else:#fase dos chutes
        print ('Você tem {0} dinheiros'.format(dinheiro))
        if dinheiro == 0:
            print ('Você perdeu')
        
        
    