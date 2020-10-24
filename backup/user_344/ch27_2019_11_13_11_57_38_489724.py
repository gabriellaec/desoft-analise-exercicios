n = int(input('quantos cigarros voce fuma? '))
anos = int(input('há quantos anos você fuma? '))
tp= n*10 *anos*365
tpm= tp*0.00069
print('você perdeu {0} dias'.format(tpm))
           