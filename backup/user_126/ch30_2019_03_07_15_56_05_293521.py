teta=int(input('angulo'))
v=int(input('velocidade'))
d=v**2*math.sin(teta)/9.8
if d >98 and d<102:
    print('Acertou!')
elif  d >95 and d<105:
    print('Muito perto')
else:
    print('Muito longe)
          