import random
dinheiro = 100
print ('você tem {0}'.format(dinheiro))
qual_aposta= input('qual aposta?(n/p) ')
if qual_aposta == 'n':
    valor = int(input('valor apostado: ')
    x=int(input('escolha um número de 1 a 36: ')
    r = random.randint(1,36)
    if x == r:
        dinheiro = dinheiro + 35*valor
    else:
        dinheiro = dinheiro - valor
elif qual_aposta == 'p':
    valor = int(input('valor apostado: ')
    tentativa = input('escolha p ou i: ')
    r = random.randint(1,36)
    if tentativa == 'p':
        if r%2 == 0:
            dinheiro = dinheiro + valor
        else:
            dinheiro = dinheiro - valor
    elif tentativa == 'i':
        if i%2 == 0:
            dinheiro = dinheiro - valor
        else:
            dinheiro = dinheiro + valor