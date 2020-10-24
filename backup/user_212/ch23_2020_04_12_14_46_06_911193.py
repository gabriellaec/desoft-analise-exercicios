velocidade=int(input('Qual a velocidade do seu carro?'))
multa=0
    
if (velocidade>80):
    multa= 5.00*velocidade 
    arredondam=round(multa,2)
    print('O usuário foi multado! Multa: R${0}'.format(arredondam)
if (velocidade<=80) :
    print('Não foi multado')