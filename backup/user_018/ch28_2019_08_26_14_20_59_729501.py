km = int(input('Qual sua velocidade?'))
if km>80:
    velocidade_extra = km - 80
    multa = velocidade_extra * 5
    print ('{0:.2f}'.format(multa))
           
else:
    print('Não foi multado')
                 
                 
    
          