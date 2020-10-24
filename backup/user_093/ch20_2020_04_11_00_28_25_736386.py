d=int(input('Qual a distância até o destino ')
	if d<= 200:
      a=0.5*d
      print('O valor é {0:.2f}'.format(a))
    else:
        a=0.45*(d-200)+100
        print('O valor é {0:.2f}'.format(a))
      