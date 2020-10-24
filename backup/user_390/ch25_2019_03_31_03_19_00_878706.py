pergunta=int(input('distancia da viagem'))
if pergunta<200:
    print(pergunta*0.5)
else:
    print(200*0.5+ (pergunta-200)*0.45)