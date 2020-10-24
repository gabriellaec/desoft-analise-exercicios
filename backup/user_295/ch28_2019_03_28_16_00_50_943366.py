velo = int (input("Qual velocidade estava o carro?"))

if velo > 80:
    
    multa = (velo - 80) * 5        
    print ("voce foi multado com um valor de {0} reais" .format (multa))
    
else: 
    print ("Não foi multado")         
            

            