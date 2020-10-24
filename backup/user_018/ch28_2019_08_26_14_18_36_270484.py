km = int(input('Qual sua velocidade?'))
if km>80:
    velocidade_extra = km - 80
    multa = velocidade_extra * 5
    print ('Você está a {0} km acima do limite, sua multa é de {1} reais'.format(velocidade_extra , multa))
           
else:
    print('Não foi multado')
                 
                 
    
          