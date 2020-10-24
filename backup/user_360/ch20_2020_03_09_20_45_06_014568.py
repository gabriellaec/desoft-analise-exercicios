dist = int(input("Qual a distância?"))
if dist <=200:
    print("Sua passagem será R$ {0:.2f}".format(dist*0.50))
else:
    print("Sua passagem será R$ {0:.2f}".format(100+ (dist-200) *0.45))