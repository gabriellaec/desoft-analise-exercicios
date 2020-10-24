velmax = float(input("Qual a velocidade máxima da via? "))
camdist = float(input("Qual a distância entre as duas câmeras? "))

placas = []
tempos = []

while True:
    placa = str(input("Qual a placa do carro? "))
    if placa == '':
        break
    placas.append(placa)
    
    t = float(input("Qual o instante que o carro passou? "))
    tempos.append(t)
    
    if len(placas) == 2:
        if placas[0] == placas[1]:
            cvel = camdist / (tempos[1] - tempos[0])
            tempos = []
            placas = []
            
            if cvel > velmax and cvel <= velmax * 1.2:
                print("Infração média. Sua penalidade é de R$130,16")
            elif cvel > velmax * 1.2 and cvel <= velmax * 1.5:
                print("Infração grave. Sua penalidade é de R$195,23")
            elif cvel > velmax * 1.5:
                print("Infração gravíssima. Sua penalidade é de 3x R$195,23 e haverá suspensão imediata do direito de dirigir a apreensão do documento de habilitação")