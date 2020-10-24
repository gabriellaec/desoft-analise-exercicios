x = int(input('Quantos cigarros você fuma por dia?'))
y = int(input('Há quantos ANOS você fuma cigarro?'))
c = x/1440
print('A quantidade de cigarros que você já fumou e fuma por dia acarretarão em uma redução de {} dias na sua vida'.format(x/1440 + y/(1440*365)))
