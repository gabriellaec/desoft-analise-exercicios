d=int(input('diatância?'))
if distância <= 200:
    passagem = 0.5 * distância
else:
    passagem = 0.45 * distância + 100
print ('{0.2f}'.format(passagem))