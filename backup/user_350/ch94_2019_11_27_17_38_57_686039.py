velocidade = int(input("qual veocidade max?"))
distancia = int(input("distancia entre as cameras?"))
while True:
    placa = input("placa do veiculo?")
    placa = str(placa)
    instante1 = int(input("instante de tempo da camera 1"))
    instante2 = int(nput("instante de tempo da camera 2"))
    if distancia/(instante2 - instante1) > velocidade and distancia/(instante2 - instante1) <= 1.2*velocidade:
        punicao = "media"
    if distancia/(instante2 - instante1) > 1.2*velocidade and velocidade and distancia/(instante2 - instante1) <= 1.5*velocidade:
        punicao = "grave"
    if velocidade and distancia/(instante2 - instante1) > 1.5*velocidade:
        punicao = "gravissima"
	if velocidade and distancia/(instante2 - instante1) < velocidade:
        punicao = "sem punicao"