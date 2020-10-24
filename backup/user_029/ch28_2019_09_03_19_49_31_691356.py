def velocidade(x):
    x=int(input('velocidade: '))
    if 60<x<=72:
        return 'média'
    elif 72<x<=90:
        return 'grave'
    elif x<=60:
        return 'ta safe'
    else: 
        return 'gravissimo'