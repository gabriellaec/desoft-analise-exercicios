distancia = float(input("Qual a distancia que voce quer percorrer?: "))
a = distancia - 200
if distancia < 200 and distancia > 0:
    print("Preço da passagem: {0:.2f}".format(distancia*0.5))
else:
    print("Preço da passagem: {0:.2f}".format((200*0.5)+a * 0.45))