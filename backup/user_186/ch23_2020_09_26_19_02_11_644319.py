velocidade = float(input ("Qual a velocidade?"))
multa = (velocidade-80)* 5
if velocidade> 80:
    print ("Você foi multado em  {:.2f} reais" .format(multa)) 
else :
    print ("Não foi multado") 