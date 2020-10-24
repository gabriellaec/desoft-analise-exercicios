km = int(input('Qual sua velocidade?'))
if km > 80:
    velocidade_extra = km - 80
    multa = velocidade_extra*5
    print ('Você está {0}km acima do limite. Sua multa é de R${1}' .format(velocidade_extra, multa))
else:
           print('Você está no limite')
           
                 
                 
                 
    
          