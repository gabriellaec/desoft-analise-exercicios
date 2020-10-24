x = int(input('Quantos cigarros você fuma por dia? '))
y = int(input('Há quantos ANOS você fuma cigarro? '))
c = x/144 * 365 * y
print('A quantidade de cigarros que você já fumou e fuma por dia acarretarão em uma redução de {0:.2f} dias na sua vida'.format(c))
