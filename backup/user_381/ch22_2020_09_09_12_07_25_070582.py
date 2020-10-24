def tempo_de_vida(cigarro,tempo):
    tp = (10/(60*24))*cigarro*(tempo*365)
    return tp

z = int(input('Quantos cigarros você fuma por dia?'))
y = int(input('Há quantos anos você fuma?'))
w = tempo_de_vida(z,y)
print(w)