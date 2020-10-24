velocidade=float(input('Qual a velocidade do seu carro?'))
multa=0
    
if (velocidade > 80):
    multa= 5.00*velocidade 
    print('O usuário foi multado! Multa: R${0:.2f}'.format(multa)
else:
    print('Não foi multado')