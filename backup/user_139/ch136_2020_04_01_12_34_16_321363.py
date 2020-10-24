dado1 = random.randit (0,6)
dado2 = random.randit (0,6)
dado3 = random.randit (0,6)
Objetivo = dado1 + dado2 + dado3
#fase de dicas:
print ('Você tem {0} dinheiros'.format(dinheiro))
if dinheiro == 0:
    print ('Você perdeu')
else:
    r1 = input ('Você quer uma dica?')
    if r1 == 'sim':
        dinheiro -= 1
        
    