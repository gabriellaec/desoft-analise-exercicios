veloc_max = int(input("Qual a velocidade máxima da via (em km/h)? "))
dist = int(input("Qual a distancia entre as câmeras (em m)? "))

placa_carro = dict()
i = True
while i != False:
    list_tempo = []
    list_placa = []
    placa = input("Qual é a placa do carro? ")
    tempo = int(input("Qual instante deseja? "))
    list_tempo.append(tempo)
    list_placa.append(placa)
    placa_carro[list_placa] = list_tempo
    soma = 0
    for e in placa_carro:
        soma += placa_carro[e]
        if not e in placa_carro:
            e = placa_carro[e]
        else:
            e = soma
        if placa_carro[e] > veloc_max or placa_carro[e] <= veloc_max*0.2:
            print("infração media - multa de (130,16 reais)")
        elif placa_carro[e] > veloc_max*0.2 or placa_carro[e] <= veloc_max*0.5:
            print("infração grave - multa de (195,23 reais)")
        elif placa_carro[e] > veloc_max*0.5:
            print("infração gravíssima - multa de (585,69 reais), suspensão do direito de dirigir e apreesão do documento de habilitação")
    if placa == "":
        i = False