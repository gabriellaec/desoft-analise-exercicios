velocidade = int(input("qual veocidade max?"))
distancia = int(input("distancia entre as cameras?"))
a = True
while a:
    placa = input("placa do veiculo?")
    placa = str(placa)
    if  not myString:
        a = False
    instante1 = int(input("instante de tempo da camera 1"))
    instante2 = int(nput("instante de tempo da camera 2"))
    V_carro = distancia/(instante2 - instante1)
    if V_carro > velocidade and V_carro <= 1.2*velocidade:
        punicao = "media"
    if V_carro > 1.2*velocidade and  V_carro <= 1.5*velocidade:
        punicao = "grave"
    if  V_carro > 1.5*velocidade:
        punicao = "gravissima"
	if V_carro < velocidade:
        punicao = "sem punicao"