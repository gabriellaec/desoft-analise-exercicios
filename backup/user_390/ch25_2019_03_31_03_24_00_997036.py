pergunta=float(input('distancia da viagem'))
if pergunta<200:
    valor=pergunta*0.5
else:
    valor=200*0.5+(pergunta-200)*0.45
print (round(valor, 2))