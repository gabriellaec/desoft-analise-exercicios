distancia= float(input('Qual distancia?: '))
if distancia <= 200:
    passagem= distancia*0.5
    print ({0:.2}.format(distancia,passagem))
else:
    passagem= (distancia- 200) *0.45 +100
    print ({0:.2}.format(distancia,passagem))
    
    