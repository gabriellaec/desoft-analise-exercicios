
v_max = float(input('Digite a velocidade máxima da via [km/h]: '))
dist = float(input('Digite a distância entre as câmeras [m]: '))

rodando = True
while rodando:
    placa = str(input('Digite a placa: '))
    if placa == "":
        rodando = False
    while len(placa) != 7:
        placa = str(input('Digite a placa: '))

    delta_t = float(input('Digite o tempo que demorou para passar entre as câmeras: ')) #segundos
    velm = dist/delta_t*3.6 #km/h

    if velm > v_max and velm <= 1.2*v_max:
        print("Infração - média\nPenalidade - multa (R$ 130,16)")
    elif velm > 1.2*v_max and velm <= 1.5*v_max:
        print("Infração - grave\nPenalidade - multa (R$ 195,23);")
    elif velm > 1.5*v_max:
        print('Infração - gravíssima\nPenalidade - multa [três vezes] (3 x R$ 195,23), suspensão imediata do direito de dirigir e apreensão do documento de habilitação.')

