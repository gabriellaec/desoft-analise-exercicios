número_de_cigarros= int(input('Quantos cigarros você fuma por dia?'))
número_de_anos= int(input('Há quantos anos você fuma?'))
redução_de_tempo_em_dias = (número_de_anos*365*número_de_cigarros*10)/(24*60)  
print(redução_de_tempo_em_dias)