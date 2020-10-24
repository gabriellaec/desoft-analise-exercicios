velocidade=float(input('Qual a sua velocidade? ')
if velocidade>80:
    multa=5*(velocidade-80)           
    print('vc foi multado')
    print ('{0:,.2f}'.format(multa))
else:
    print('Não foi multado')
               
               