pergunta= int(input('Quantos cigarros você fuma por dia?'))
pergunta2= int(input('Há quantos anos você fuma?'))
minutos_para_dias= 0.00694444
dias_perdidos= pergunta*pergunta2*minutos_para_dias

def calculo_dias(dias_perdidos):
    if pergunta2 and pergunta >= 1:
     dias_perdidos= pergunta*pergunta2*minutos_para_dias
     return dias_perdidos
    else:
      return 'Insira um número maior que esse'
print(calculo_dias(dias_perdidos))
    


